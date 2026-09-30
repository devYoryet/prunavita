#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Sincroniza el bloque "Ultimas publicaciones" de la portada con el hub de noticias.

Por que existe: la portada decia "Ultimas Publicaciones" y mostraba una copia a
mano de un post de LinkedIn de junio, con la antiguedad escrita dura ("1 dia").
Llevaba meses afirmando que el post era de ayer, y la portada --que es la pagina
con mas autoridad del sitio-- no enlazaba NINGUNA noticia propia. Cada noticia
nueva nacia sin un solo enlace desde la home.

Escribirlo a mano lo habria arreglado hoy y lo habria roto en la proxima noticia.
Por eso se genera: las tarjetas salen de /noticias/index.html, que es la unica
fuente de verdad del orden editorial.

Uso
---
  python scripts/ultimas_publicaciones.py            # actualiza index.html
  python scripts/ultimas_publicaciones.py --revisar  # solo informa, no escribe

Se ejecuta solo en cada commit a traves del hook pre-commit.
"""

import argparse
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

RAIZ = Path(__file__).resolve().parent.parent
HUB = RAIZ / "noticias" / "index.html"
PORTADA = RAIZ / "index.html"
INICIO = "<!-- ULTIMAS:INICIO -->"
FIN = "<!-- ULTIMAS:FIN -->"
CUANTAS = 3

MESES = ("enero febrero marzo abril mayo junio julio agosto septiembre "
         "octubre noviembre diciembre").split()


def _uno(patron, texto, grupo=1):
    m = re.search(patron, texto, re.S)
    return m.group(grupo).strip() if m else None


def noticias():
    """Lee el hub y devuelve las noticias en orden editorial."""
    html = HUB.read_text(encoding="utf-8")
    bloques = re.findall(
        r'<article class="news-featured">(.*?)</article>|'
        r'<article class="news-card news-card--hub">(.*?)</article>',
        html, re.S)

    salida = []
    for destacada, tarjeta in bloques:
        b = destacada or tarjeta
        url = _uno(r'href="(/noticias/[^"]+\.html)"', b)
        img = _uno(r'<img src="\.\./([^"]+)"', b)
        alt = _uno(r'<img [^>]*alt="([^"]*)"', b)
        cat = _uno(r'<span class="news-category">([^<]+)</span>', b)
        fecha = _uno(r'<time datetime="([^"]+)"', b)
        legible = _uno(r'<time[^>]*>([^<]+)</time>', b)
        titulo = _uno(r'<h2><a href="[^"]*">(.*?)</a></h2>', b)
        resumen = _uno(r'<p>\s*(.*?)\s*</p>', b)
        if not (url and titulo and fecha):
            continue
        salida.append({"url": url, "img": img, "alt": alt or "", "cat": cat or "Noticias",
                       "fecha": fecha, "legible": legible or fecha,
                       "titulo": titulo, "resumen": re.sub(r"\s+", " ", resumen or "")})
    salida.sort(key=lambda n: n["fecha"], reverse=True)
    return salida


def tarjeta(n):
    resumen = n["resumen"]
    if len(resumen) > 190:
        corte = resumen[:190].rsplit(" ", 1)[0]
        resumen = corte + "&hellip;"
    return (
        '                <article class="news-card news-card--hub">\n'
        f'                    <a class="news-card-thumb" href="{n["url"]}">\n'
        f'                        <img src="{n["img"]}" alt="{n["alt"]}" loading="lazy">\n'
        '                    </a>\n'
        '                    <div class="news-card-body">\n'
        '                        <div class="news-meta">\n'
        f'                            <span class="news-category">{n["cat"]}</span> &middot; '
        f'<time datetime="{n["fecha"]}">{n["legible"]}</time>\n'
        '                        </div>\n'
        f'                        <h3><a href="{n["url"]}">{n["titulo"]}</a></h3>\n'
        f'                        <p>{resumen}</p>\n'
        f'                        <a class="news-link" href="{n["url"]}">Leer m&aacute;s &rarr;</a>\n'
        '                    </div>\n'
        '                </article>\n'
    )


def bloque(lista):
    tarjetas = "".join(tarjeta(n) for n in lista[:CUANTAS])
    return (
        f"{INICIO}\n"
        '            <div class="news-grid">\n'
        f"{tarjetas}"
        '            </div>\n'
        f"            {FIN}"
    )


def main():
    ap = argparse.ArgumentParser(description="Sincroniza las ultimas publicaciones de la portada")
    ap.add_argument("--revisar", action="store_true", help="Solo informa; no escribe")
    args = ap.parse_args()

    lista = noticias()
    if not lista:
        sys.exit("[ERROR] No se pudo leer ninguna noticia de noticias/index.html")

    texto = PORTADA.read_text(encoding="utf-8")
    if INICIO not in texto or FIN not in texto:
        sys.exit(f"[ERROR] La portada no tiene los marcadores {INICIO} / {FIN}")

    nuevo = bloque(lista)
    actual = texto[texto.index(INICIO):texto.index(FIN) + len(FIN)]

    print("Ultimas publicaciones segun el hub:")
    for n in lista[:CUANTAS]:
        print(f"   {n['fecha']}  {n['titulo'][:62]}")

    if actual.strip() == nuevo.strip():
        print("\n[OK] La portada ya muestra las ultimas publicaciones.")
        return 0

    print("\nLa portada estaba desactualizada.")
    if args.revisar:
        return 1

    PORTADA.write_text(texto.replace(actual, nuevo, 1), encoding="utf-8")
    print("[OK] index.html actualizado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
