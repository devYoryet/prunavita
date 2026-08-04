#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Seguimiento SEO diario — Prunavita.cl

Toma una foto diaria de Google Search Console y la acumula en un historico.
Sin historico no hay forma de saber si una palanca funciono o no.

La metrica norte del proyecto (ago 2026) es CLICS NO-MARCA: hoy en 0.
Todo el trafico actual viene de gente que busca "prunavita" por su nombre.

Uso
---
  python scripts/seguimiento_seo.py foto        # snapshot de hoy -> historico.csv
  python scripts/seguimiento_seo.py resumen     # tendencia acumulada
  python scripts/seguimiento_seo.py objetivos   # posicion de las keywords objetivo
  python scripts/seguimiento_seo.py todo        # las tres

Ojo con los datos: Search Console tiene 2-3 dias de retraso y oculta las
consultas de bajo volumen ("anonimizadas"). Por eso los clics del total
no cuadran con la suma de clics por consulta. Ambos numeros se registran.
"""

import argparse
import csv
import datetime
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

RAIZ = Path(__file__).resolve().parent.parent
DIR_SEG = RAIZ / "seo-system" / "seguimiento"
HISTORICO = DIR_SEG / "historico.csv"
SITIO = "sc-domain:prunavita.cl"

# Se considera marca cualquier consulta que nombre a la empresa.
MARCA = ("prunavita", "pruna vita", "prunaVita".lower())

# Keywords objetivo: las que GSC ya muestra con intencion comercial.
# Mover estas es el trabajo de agosto-septiembre 2026.
OBJETIVOS = [
    "certificación brc chile",
    "compra maquinaria usada",
    "venta maquinaria manufactura",
    "consultoría agroindustria",
    "asesoría en certificaciones",
]

COLUMNAS = [
    "fecha_snapshot", "ventana_dias", "clics_total", "impresiones_total",
    "ctr_total", "posicion_media", "consultas_reveladas", "clics_marca",
    "clics_no_marca", "impresiones_no_marca", "paginas_con_impresiones",
]


def servicio():
    from google.oauth2 import service_account
    from googleapiclient.discovery import build

    clave = None
    for p in RAIZ.glob("*.json"):
        if p.name in {"vercel.json", "site.webmanifest"} or p.name.startswith("client_secret"):
            continue
        try:
            if json.loads(p.read_text(encoding="utf-8")).get("type") == "service_account":
                clave = p
                break
        except (ValueError, OSError):
            continue

    if clave is None:
        sys.exit("[ERROR] No se encontro la clave de cuenta de servicio en la raiz del proyecto.")

    creds = service_account.Credentials.from_service_account_file(
        str(clave), scopes=["https://www.googleapis.com/auth/webmasters.readonly"])
    return build("searchconsole", "v1", credentials=creds, cache_discovery=False)


def consultar(svc, dims, dias, limite=500):
    hoy = datetime.date.today()
    body = {
        "startDate": (hoy - datetime.timedelta(days=dias)).isoformat(),
        "endDate": hoy.isoformat(),
        "dimensions": dims,
        "rowLimit": limite,
    }
    return svc.searchanalytics().query(siteUrl=SITIO, body=body).execute().get("rows", [])


def es_marca(consulta):
    c = consulta.lower()
    return any(m in c for m in MARCA)


# ---------------------------------------------------------------- comandos

def cmd_foto(args):
    svc = servicio()
    dias = args.ventana

    por_fecha = consultar(svc, ["date"], dias)
    consultas = consultar(svc, ["query"], dias)
    paginas = consultar(svc, ["page"], dias)

    clics = sum(f["clicks"] for f in por_fecha)
    impr = sum(f["impressions"] for f in por_fecha)
    # Posicion media ponderada por impresiones (no promedio simple).
    pos = (sum(f["position"] * f["impressions"] for f in por_fecha) / impr) if impr else 0

    no_marca = [f for f in consultas if not es_marca(f["keys"][0])]
    marca = [f for f in consultas if es_marca(f["keys"][0])]

    fila = {
        "fecha_snapshot": datetime.date.today().isoformat(),
        "ventana_dias": dias,
        "clics_total": clics,
        "impresiones_total": impr,
        "ctr_total": round(100 * clics / impr, 2) if impr else 0,
        "posicion_media": round(pos, 1),
        "consultas_reveladas": len(consultas),
        "clics_marca": sum(f["clicks"] for f in marca),
        "clics_no_marca": sum(f["clicks"] for f in no_marca),
        "impresiones_no_marca": sum(f["impressions"] for f in no_marca),
        "paginas_con_impresiones": len(paginas),
    }

    DIR_SEG.mkdir(parents=True, exist_ok=True)
    nuevo = not HISTORICO.exists()
    with HISTORICO.open("a", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNAS)
        if nuevo:
            w.writeheader()
        w.writerow(fila)

    print(f"Foto guardada — {fila['fecha_snapshot']} (ventana {dias} dias)\n")
    print(f"  Clics totales           {fila['clics_total']}")
    print(f"  Impresiones             {fila['impresiones_total']}")
    print(f"  CTR                     {fila['ctr_total']}%")
    print(f"  Posicion media          {fila['posicion_media']}")
    print(f"  Consultas reveladas     {fila['consultas_reveladas']}")
    print(f"  Paginas con impresiones {fila['paginas_con_impresiones']}")
    print()
    print(f"  >> CLICS NO-MARCA       {fila['clics_no_marca']}   <-- metrica norte")
    print(f"     Clics de marca       {fila['clics_marca']}")
    print(f"     (la diferencia con el total son consultas que Google oculta)")
    print(f"\n  -> {HISTORICO.relative_to(RAIZ)}")


def leer_historico():
    if not HISTORICO.exists():
        sys.exit("[ERROR] Todavia no hay historico. Corre primero:  python scripts/seguimiento_seo.py foto")
    with HISTORICO.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def cmd_resumen(args):
    filas = leer_historico()
    print(f"Historico: {len(filas)} fotos, de {filas[0]['fecha_snapshot']} a {filas[-1]['fecha_snapshot']}\n")

    cab = f"{'FECHA':<12}{'CLICS':>7}{'IMPR':>7}{'NO-MARCA':>10}{'CONSULTAS':>11}{'POS':>7}"
    print(cab)
    print("-" * len(cab))
    for f in filas:
        print(f"{f['fecha_snapshot']:<12}{f['clics_total']:>7}{f['impresiones_total']:>7}"
              f"{f['clics_no_marca']:>10}{f['consultas_reveladas']:>11}{f['posicion_media']:>7}")

    if len(filas) < 2:
        print("\n(Con una sola foto no hay tendencia todavia. Vuelve manana.)")
        return

    ini, fin = filas[0], filas[-1]
    print("\nVariacion desde la primera foto:")
    for campo, etiqueta in (("impresiones_total", "Impresiones"),
                            ("clics_total", "Clics"),
                            ("consultas_reveladas", "Consultas distintas"),
                            ("clics_no_marca", "Clics NO-MARCA")):
        a, b = float(ini[campo]), float(fin[campo])
        delta = f"{100*(b-a)/a:+.0f}%" if a else ("nuevo" if b else "sin cambio")
        print(f"  {etiqueta:<22} {a:>6.0f} -> {b:>6.0f}   {delta}")


def cmd_objetivos(args):
    svc = servicio()
    filas = consultar(svc, ["query"], args.ventana)
    mapa = {f["keys"][0].lower(): f for f in filas}

    print(f"Keywords objetivo — ventana {args.ventana} dias\n")
    cab = f"{'CONSULTA':<34}{'POS':>7}{'IMPR':>7}{'CLICS':>7}   ESTADO"
    print(cab)
    print("-" * (len(cab) + 8))
    for kw in OBJETIVOS:
        f = mapa.get(kw)
        if not f:
            print(f"{kw:<34}{'—':>7}{'—':>7}{'—':>7}   sin impresiones en la ventana")
            continue
        pos = f["position"]
        if pos <= 10:
            estado = "PRIMERA PAGINA"
        elif pos <= 20:
            estado = "segunda pagina — cerca"
        elif pos <= 40:
            estado = "en camino"
        else:
            estado = "lejos"
        print(f"{kw:<34}{pos:>7.1f}{f['impressions']:>7}{f['clicks']:>7}   {estado}")

    print("\nMeta ago-sep 2026: mover estas consultas al rango 15-25 y")
    print("conseguir los primeros clics no-marca (hoy 0).")


def main():
    p = argparse.ArgumentParser(description="Seguimiento SEO diario de Prunavita.cl")
    sub = p.add_subparsers(dest="comando", required=True)

    a = sub.add_parser("foto", help="Guarda el snapshot de hoy en el historico")
    a.add_argument("--ventana", type=int, default=28, help="Dias hacia atras (def. 28)")
    a.set_defaults(func=cmd_foto)

    a = sub.add_parser("resumen", help="Muestra la tendencia acumulada")
    a.set_defaults(func=cmd_resumen)

    a = sub.add_parser("objetivos", help="Posicion actual de las keywords objetivo")
    a.add_argument("--ventana", type=int, default=90)
    a.set_defaults(func=cmd_objetivos)

    a = sub.add_parser("todo", help="foto + resumen + objetivos")
    a.add_argument("--ventana", type=int, default=28)
    a.set_defaults(func=lambda ar: (cmd_foto(ar), print("\n" + "="*70 + "\n"),
                                    cmd_resumen(ar), print("\n" + "="*70 + "\n"),
                                    cmd_objetivos(argparse.Namespace(ventana=90))))

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
