#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Medicion mensual — Prunavita.cl

Un solo comando con todo lo que hace falta para cerrar el mes: Search Console,
GA4 y el cruce de ambos por pagina de entrada. Existe para no volver a
reconstruir a mano lo que se armo el 29 de agosto de 2026.

Uso
---
  python scripts/medicion_mensual.py                 # mes en curso vs el anterior
  python scripts/medicion_mensual.py --mes 2026-08   # un mes concreto
  python scripts/medicion_mensual.py --estado        # solo diagnostico de accesos

Donde mirar cuando algo falla
-----------------------------
GSC y GA4 se leen con la cuenta de servicio claude@android-1428a.iam.gserviceaccount.com.
Si una llamada devuelve 403, el motivo real viene en el JSON del error:

  reason=SERVICE_DISABLED   -> la API esta apagada en el proyecto de Google Cloud.
                               Se habilita sin consola con --habilitar (la cuenta de
                               servicio tiene permiso sobre el proyecto).
  reason=PERMISSION_DENIED  -> la API esta activa pero falta dar acceso a la cuenta
                               de servicio en GSC o en GA4. Eso si lo hace el cliente.

El vinculo GA4 <-> Search Console NO lo expone la Admin API. No concluir que falta
porque no aparece: se comprueba pidiendo las metricas organicGoogleSearch* con la
dimension landingPagePlusQueryString (es lo que hace el bloque de cruce).
"""

import argparse
import calendar
import datetime
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

RAIZ = Path(__file__).resolve().parent.parent
CLAVE = RAIZ / "android-1428a-8f4640cb2bd7.json"

SITIO_GSC = "sc-domain:prunavita.cl"
PROPIEDAD_GA4 = "properties/541942768"          # propiedad "prunavita", flujo G-0G9GQYN4RE
PROYECTO_CLOUD = "projects/601992161161"        # android-1428a
APIS = ["analyticsadmin.googleapis.com", "analyticsdata.googleapis.com"]

# GSC consolida con 2-3 dias de retraso; se corta la ventana para no leer dias a medias.
DIAS_RETRASO_GSC = 3


def credenciales(cloud=False):
    if cloud:
        ambitos = ["https://www.googleapis.com/auth/cloud-platform"]
    else:
        ambitos = ["https://www.googleapis.com/auth/analytics.readonly",
                   "https://www.googleapis.com/auth/webmasters.readonly"]
    return service_account.Credentials.from_service_account_file(str(CLAVE), scopes=ambitos)


def motivo(e):
    """Extrae el motivo real de un error de Google, no el mensaje generico."""
    try:
        err = json.loads(e.content.decode("utf-8"))["error"]
        razones = [d.get("reason") for d in err.get("details", []) if d.get("reason")]
        return f"{err.get('code')} {err.get('status')} [{','.join(razones) or '-'}] {err.get('message', '')[:200]}"
    except Exception:
        return str(e)[:200]


# ---------------------------------------------------------------- diagnostico

def estado(habilitar=False):
    print("== Estado de las APIs en Google Cloud ==")
    su = build("serviceusage", "v1", credentials=credenciales(cloud=True), cache_discovery=False)
    for api in APIS:
        try:
            st = su.services().get(name=f"{PROYECTO_CLOUD}/services/{api}").execute().get("state")
            print(f"  {api:34} {st}")
            if st == "DISABLED" and habilitar:
                su.services().enable(name=f"{PROYECTO_CLOUD}/services/{api}", body={}).execute()
                print(f"  {'':34} -> solicitud de habilitacion enviada (tarda 1-2 min)")
        except HttpError as e:
            print(f"  {api:34} no se pudo consultar: {motivo(e)}")

    print("\n== Acceso a las propiedades ==")
    creds = credenciales()
    try:
        sc = build("searchconsole", "v1", credentials=creds, cache_discovery=False)
        sitios = [s["siteUrl"] for s in sc.sites().list().execute().get("siteEntry", [])]
        print(f"  GSC : {'OK' if SITIO_GSC in sitios else 'SIN ACCESO A ' + SITIO_GSC}")
    except HttpError as e:
        print(f"  GSC : {motivo(e)}")
    try:
        admin = build("analyticsadmin", "v1beta", credentials=creds, cache_discovery=False)
        props = [p.get("property")
                 for a in admin.accountSummaries().list().execute().get("accountSummaries", [])
                 for p in a.get("propertySummaries", [])]
        print(f"  GA4 : {'OK' if PROPIEDAD_GA4 in props else 'SIN ACCESO A ' + PROPIEDAD_GA4}")
    except HttpError as e:
        print(f"  GA4 : {motivo(e)}")


# ---------------------------------------------------------------- consultas

def rango(mes):
    ano, m = (int(x) for x in mes.split("-"))
    ini = datetime.date(ano, m, 1)
    fin = datetime.date(ano, m, calendar.monthrange(ano, m)[1])
    tope = datetime.date.today() - datetime.timedelta(days=DIAS_RETRASO_GSC)
    return ini, min(fin, tope)


def gsc_total(sc, a, b):
    r = sc.searchanalytics().query(
        siteUrl=SITIO_GSC, body={"startDate": str(a), "endDate": str(b), "rowLimit": 1}).execute()
    f = r.get("rows", [])
    return f[0] if f else {}


def gsc_interiores(sc, a, b):
    r = sc.searchanalytics().query(siteUrl=SITIO_GSC, body={
        "startDate": str(a), "endDate": str(b), "dimensions": ["page"], "rowLimit": 500}).execute()
    filas = r.get("rows", [])
    inter = sum(x["clicks"] for x in filas
                if x["keys"][0].rstrip("/") != "https://prunavita.cl")
    return inter, len(filas)


def ga4_informe(data, dims, mets, a, b, filtro=None, limite=50):
    cuerpo = {"dateRanges": [{"startDate": str(a), "endDate": str(b)}],
              "dimensions": [{"name": d} for d in dims],
              "metrics": [{"name": m} for m in mets], "limit": limite}
    if filtro:
        cuerpo["dimensionFilter"] = filtro
    return data.properties().runReport(property=PROPIEDAD_GA4, body=cuerpo).execute()


def valor(fila, i):
    return float(fila["metricValues"][i]["value"])


def medir(mes):
    creds = credenciales()
    sc = build("searchconsole", "v1", credentials=creds, cache_discovery=False)
    data = build("analyticsdata", "v1beta", credentials=creds, cache_discovery=False)

    ini, fin = rango(mes)
    ano, m = (int(x) for x in mes.split("-"))
    prev = f"{ano - 1}-12" if m == 1 else f"{ano}-{m - 1:02d}"
    p_ini, _ = rango(prev)
    # Misma cantidad de dias en ambos meses: comparar 25 dias contra 31 no dice nada.
    dias = (fin - ini).days
    p_fin = p_ini + datetime.timedelta(days=dias)

    print(f"\n{'=' * 78}")
    print(f"MEDICION {mes}  ({ini} a {fin}, {dias + 1} dias)")
    print(f"Se compara contra {prev} en la misma ventana ({p_ini} a {p_fin})")
    print("=" * 78)

    print("\n== Search Console ==")
    print(f"  {'':10} {'clics':>7} {'impr':>8} {'CTR%':>7} {'pos':>6} {'inter':>7} {'pags':>6}")
    for etiqueta, a, b in ((prev, p_ini, p_fin), (mes, ini, fin)):
        t = gsc_total(sc, a, b)
        inter, pags = gsc_interiores(sc, a, b)
        print(f"  {etiqueta:10} {t.get('clicks', 0):7.0f} {t.get('impressions', 0):8.0f} "
              f"{t.get('ctr', 0) * 100:7.2f} {t.get('position', 0):6.1f} {inter:7.0f} {pags:6.0f}")
    print("  inter = clics que NO cayeron en la home (metrica norte del plan)")

    print("\n== GA4 — sesiones y usuarios ==")
    print(f"  {'':10} {'sesiones':>9} {'usuarios':>9} {'vistas':>8} {'eventos':>9}")
    for etiqueta, a, b in ((prev, p_ini, p_fin), (mes, ini, fin)):
        f = ga4_informe(data, [], ["sessions", "totalUsers", "screenPageViews", "eventCount"], a, b)
        filas = f.get("rows", [])
        if filas:
            r = filas[0]
            print(f"  {etiqueta:10} {valor(r, 0):9.0f} {valor(r, 1):9.0f} {valor(r, 2):8.0f} {valor(r, 3):9.0f}")

    print("\n== GA4 — canales ==")
    for r in ga4_informe(data, ["sessionDefaultChannelGroup"], ["sessions", "totalUsers"],
                         ini, fin, limite=15).get("rows", []):
        print(f"  {r['dimensionValues'][0]['value']:24} sesiones={valor(r, 0):.0f} usuarios={valor(r, 1):.0f}")

    print("\n== GA4 — contactos iniciados (WhatsApp / correo / formulario) ==")
    filtro = {"filter": {"fieldName": "eventName", "stringFilter": {"value": "contacto_iniciado"}}}
    filas = ga4_informe(data, ["date", "pagePath", "sessionDefaultChannelGroup"],
                        ["eventCount"], ini, fin, filtro).get("rows", [])
    if not filas:
        print("  ninguno en el periodo")
    for r in filas:
        d = [v["value"] for v in r["dimensionValues"]]
        print(f"  {d[0]}  {d[1][:52]:52} {d[2]:16} x{valor(r, 0):.0f}")

    print("\n== Cruce por pagina de entrada (requiere el vinculo GA4 <-> Search Console) ==")
    try:
        busq = ga4_informe(data, ["landingPagePlusQueryString"],
                           ["organicGoogleSearchClicks", "organicGoogleSearchImpressions",
                            "organicGoogleSearchClickThroughRate", "organicGoogleSearchAveragePosition"],
                           ini, fin)
        uso = ga4_informe(data, ["landingPagePlusQueryString"],
                          ["sessions", "engagementRate", "userEngagementDuration"], ini, fin, limite=100)
        idx = {}
        for r in uso.get("rows", []):
            s = valor(r, 0)
            idx[r["dimensionValues"][0]["value"]] = (s, valor(r, 1), valor(r, 2) / s if s else 0)
        filas = busq.get("rows", [])
        if not filas:
            print("  sin datos. Si nunca devuelve filas, revisar el vinculo en")
            print("  GA4 > Administrar > Vinculaciones de productos > Search Console")
        print(f"  {'pagina':50} {'clics':>6} {'impr':>7} {'CTR%':>6} {'pos':>5} {'ses':>5} {'engag%':>7} {'s/ses':>6}")
        for r in filas:
            k = r["dimensionValues"][0]["value"]
            if valor(r, 1) < 2:
                continue
            s, er, seg = idx.get(k, (0, 0, 0))
            print(f"  {k[:50]:50} {valor(r, 0):6.0f} {valor(r, 1):7.0f} {valor(r, 2) * 100:6.2f} "
                  f"{valor(r, 3):5.1f} {s:5.0f} {er * 100:7.1f} {seg:6.0f}")
    except HttpError as e:
        print(f"  no se pudo cruzar: {motivo(e)}")


def main():
    hoy = datetime.date.today()
    ap = argparse.ArgumentParser(description="Medicion mensual de Prunavita (GSC + GA4)")
    ap.add_argument("--mes", default=f"{hoy.year}-{hoy.month:02d}", help="AAAA-MM")
    ap.add_argument("--estado", action="store_true", help="solo diagnostico de accesos")
    ap.add_argument("--habilitar", action="store_true", help="habilitar las APIs apagadas")
    args = ap.parse_args()

    if args.estado or args.habilitar:
        estado(habilitar=args.habilitar)
        return
    try:
        medir(args.mes)
    except HttpError as e:
        print(f"\nFallo la medicion: {motivo(e)}")
        print("Corre: python scripts/medicion_mensual.py --estado")
        sys.exit(1)


if __name__ == "__main__":
    main()
