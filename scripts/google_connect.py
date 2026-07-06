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

SCOPES = [
    "https://www.googleapis.com/auth/webmasters.readonly",
    "https://www.googleapis.com/auth/analytics.readonly",
]


def find_client_secret() -> Path:
    if not CLIENT_GLOB:
        print("No se encontró client_secret*.json en la raíz del proyecto.")
        sys.exit(1)
    return CLIENT_GLOB[0]


def get_credentials():
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
            print("Si falla, agregue http://localhost:8090/ en Google Cloud Console > OAuth > URIs de redireccion.\n")
            creds = flow.run_local_server(port=8090, open_browser=True)
        TOKEN_PATH.write_text(creds.to_json(), encoding="utf-8")
        print(f"Token guardado en {TOKEN_PATH.name}")

    return creds


def check_search_console(creds) -> None:
    from googleapiclient.discovery import build

    service = build("searchconsole", "v1", credentials=creds, cache_discovery=False)
    sites = service.sites().list().execute()
    entries = sites.get("siteEntry", [])

    print("\n=== Google Search Console ===")
    if not entries:
        print("Sin propiedades. Verifique prunavita.cl en https://search.google.com/search-console")
        return

    for site in entries:
        print(f"  • {site.get('siteUrl')} — permiso: {site.get('permissionLevel')}")


def check_analytics(creds) -> None:
    from googleapiclient.discovery import build

    admin = build("analyticsadmin", "v1beta", credentials=creds, cache_discovery=False)
    accounts = admin.accounts().list().execute()
    account_list = accounts.get("accounts", [])

    print("\n=== Google Analytics (GA4) ===")
    if not account_list:
        print("Sin cuentas de Analytics visibles para este usuario.")
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


def main() -> None:
    creds = get_credentials()
    check_search_console(creds)
    check_analytics(creds)
    print("\nListo. Puede volver a ejecutar este script sin re-autorizar.\n")


if __name__ == "__main__":
    main()
