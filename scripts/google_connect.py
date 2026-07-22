#!/usr/bin/env python3
"""
Conexión OAuth a Google Search Console y Google Analytics (GA4).
Uso (desde la raíz del proyecto):
  python scripts/google_connect.py

Requisito en Google Cloud Console:
  - APIs habilitadas: Search Console API + Google Analytics Data API
  - En el cliente OAuth "Web", agregar URI de redirección:
    http://localhost:8090/
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKEN_PATH = ROOT / ".google-token.json"
CLIENT_GLOB = list(ROOT.glob("client_secret*.json"))
# Clave de cuenta de servicio (preferida: no requiere navegador). Debe estar en .gitignore.
SA_GLOB = [
    p for p in ROOT.glob("*.json")
    if p.name not in {"vercel.json", "site.webmanifest"}
    and not p.name.startswith("client_secret")
]

SCOPES = [
    "https://www.googleapis.com/auth/webmasters.readonly",
    "https://www.googleapis.com/auth/analytics.readonly",
]


def _service_account_key() -> Path | None:
    """Devuelve la primera clave JSON de tipo 'service_account' en la raíz."""
    for path in SA_GLOB:
        try:
            if json.loads(path.read_text(encoding="utf-8")).get("type") == "service_account":
                return path
        except (ValueError, OSError):
            continue
    return None


def find_client_secret() -> Path:
    if not CLIENT_GLOB:
        print("No se encontró client_secret*.json en la raíz del proyecto.")
        sys.exit(1)
    return CLIENT_GLOB[0]


def get_credentials():
    # 1) Preferir cuenta de servicio (sin navegador, reusable, ideal para reportes).
    sa_key = _service_account_key()
    if sa_key is not None:
        from google.oauth2 import service_account

        print(f"Autenticando con cuenta de servicio: {sa_key.name}")
        creds = service_account.Credentials.from_service_account_file(
            str(sa_key), scopes=SCOPES
        )
        print(f"  → {creds.service_account_email}")
        print("  (Debe estar agregada como usuario en GSC y como Lector en GA4.)")
        return creds

    # 2) Si no hay cuenta de servicio, caer al flujo OAuth de usuario.
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow

    creds = None
    if TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                str(find_client_secret()), SCOPES
            )
            print("\nAbriendo navegador para autorizar acceso a Google...")
            print("Si falla, agregue http://localhost:8091/ en Google Cloud Console > OAuth > URIs de redireccion.\n")
            creds = flow.run_local_server(port=8091, open_browser=False, prompt="consent")
        TOKEN_PATH.write_text(creds.to_json(), encoding="utf-8")
        print(f"Token guardado en {TOKEN_PATH.name}")

    return creds


def _date_range(days: int = 28):
    import datetime

    end = datetime.date.today()
    start = end - datetime.timedelta(days=days)
    return start.isoformat(), end.isoformat()


def check_search_console(creds) -> None:
    from googleapiclient.discovery import build

    service = build("searchconsole", "v1", credentials=creds, cache_discovery=False)
    sites = service.sites().list().execute()
    entries = sites.get("siteEntry", [])

    print("\n=== Google Search Console ===")
    if not entries:
        print("Sin propiedades verificadas para este usuario.")
        print("→ Verifique prunavita.cl en https://search.google.com/search-console")
        print("  (Prefijo de URL 'https://prunavita.cl/' + Etiqueta HTML — el meta ya está desplegado).")
        return

    for site in entries:
        print(f"  • {site.get('siteUrl')} — permiso: {site.get('permissionLevel')}")

    # Buscar la propiedad de prunavita y traer datos de rendimiento (últimos 28 días)
    target = None
    for site in entries:
        url = site.get("siteUrl", "")
        if "prunavita" in url:
            target = url
            break
    if not target:
        print("  (No se encontró una propiedad de prunavita.cl para consultar rendimiento.)")
        return

    start, end = _date_range(28)
    print(f"\n  Rendimiento de {target} — {start} a {end}:")
    for dim, titulo in (("query", "Top consultas (keywords)"), ("page", "Top páginas")):
        try:
            resp = (
                service.searchanalytics()
                .query(
                    siteUrl=target,
                    body={
                        "startDate": start,
                        "endDate": end,
                        "dimensions": [dim],
                        "rowLimit": 15,
                    },
                )
                .execute()
            )
            rows = resp.get("rows", [])
            print(f"\n  — {titulo} —")
            if not rows:
                print("    (Sin datos aún: la propiedad es nueva o Google todavía no indexa/registra búsquedas.)")
                continue
            for r in rows:
                key = r["keys"][0]
                print(
                    f"    {key[:70]:70} clics={int(r.get('clicks',0))} "
                    f"impr={int(r.get('impressions',0))} pos={r.get('position',0):.1f}"
                )
        except Exception as exc:  # noqa: BLE001
            print(f"    No se pudo consultar '{dim}': {exc}")


def check_analytics(creds) -> None:
    from googleapiclient.discovery import build

    print("\n=== Google Analytics (GA4) ===")
    admin = build("analyticsadmin", "v1beta", credentials=creds, cache_discovery=False)
    try:
        accounts = admin.accounts().list().execute()
    except Exception as exc:  # noqa: BLE001
        msg = str(exc)
        if "has not been used" in msg or "is disabled" in msg or "403" in msg:
            print("  No se pudo leer GA4. Falta un paso de configuración:")
            print("  1) Habilitar 'Google Analytics Admin API' y 'Google Analytics Data API'")
            print("     en https://console.cloud.google.com (proyecto android-1428a).")
            print("  2) Agregar la cuenta de servicio como 'Lector' en GA4")
            print("     (Administrar → Gestión de accesos a la cuenta/propiedad).")
        else:
            print(f"  Error GA4: {msg[:200]}")
        return
    account_list = accounts.get("accounts", [])

    if not account_list:
        print("Sin cuentas de Analytics visibles para esta cuenta de servicio.")
        print("→ Agregue la cuenta de servicio como 'Lector' en GA4.")
        return

    for account in account_list:
        name = account.get("name")
        display = account.get("displayName", name)
        print(f"  Cuenta: {display}")

        props = (
            admin.properties()
            .list(filter=f"parent:{name}", pageSize=50)
            .execute()
        )
        for prop in props.get("properties", []):
            pid = prop.get("name", "").split("/")[-1]
            print(f"    • {prop.get('displayName')} (ID: {pid}) — {prop.get('propertyType', '')}")
            _ga4_report(creds, pid)


def _ga4_report(creds, property_id: str) -> None:
    """Reporte rápido GA4 (últimos 28 días): usuarios, sesiones, top páginas y canales."""
    from googleapiclient.discovery import build

    data = build("analyticsdata", "v1beta", credentials=creds, cache_discovery=False)
    start, end = _date_range(28)

    # Totales: usuarios activos y sesiones
    try:
        totals = (
            data.properties()
            .runReport(
                property=f"properties/{property_id}",
                body={
                    "dateRanges": [{"startDate": start, "endDate": end}],
                    "metrics": [{"name": "activeUsers"}, {"name": "sessions"}],
                },
            )
            .execute()
        )
        rows = totals.get("rows", [])
        if rows:
            vals = rows[0].get("metricValues", [])
            usuarios = vals[0].get("value", "0") if len(vals) > 0 else "0"
            sesiones = vals[1].get("value", "0") if len(vals) > 1 else "0"
            print(f"        ¿Alguien entró? últimos 28 días → usuarios={usuarios}, sesiones={sesiones}")
        else:
            print("        Sin sesiones registradas en los últimos 28 días.")
    except Exception as exc:  # noqa: BLE001
        print(f"        No se pudo leer GA4 (¿API 'Google Analytics Data' habilitada?): {exc}")
        return

    # Top páginas y canales de adquisición
    for dim, metric, titulo in (
        ("pagePath", "screenPageViews", "Top páginas"),
        ("sessionDefaultChannelGroup", "sessions", "Canales (de dónde llegan)"),
    ):
        try:
            resp = (
                data.properties()
                .runReport(
                    property=f"properties/{property_id}",
                    body={
                        "dateRanges": [{"startDate": start, "endDate": end}],
                        "dimensions": [{"name": dim}],
                        "metrics": [{"name": metric}],
                        "limit": 8,
                    },
                )
                .execute()
            )
            rows = resp.get("rows", [])
            if not rows:
                continue
            print(f"        {titulo}:")
            for r in rows:
                k = r.get("dimensionValues", [{}])[0].get("value", "")
                v = r.get("metricValues", [{}])[0].get("value", "0")
                print(f"          {k[:60]:60} {v}")
        except Exception:  # noqa: BLE001
            pass


def main() -> None:
    # La consola de Windows (cp1252) no encoda •, → ni acentos. Forzar UTF-8.
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    creds = get_credentials()
    check_search_console(creds)
    check_analytics(creds)
    print("\nListo. Puede volver a ejecutar este script sin re-autorizar.\n")


if __name__ == "__main__":
    main()
