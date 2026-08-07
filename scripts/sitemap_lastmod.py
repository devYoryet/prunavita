#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Sincroniza el <lastmod> del sitemap con la fecha real de cambio de cada archivo.

Por que existe: el sitemap declaraba que las paginas de servicio no cambiaban
desde junio, cuando se habian ampliado en agosto. Google usa lastmod como una
senal para decidir que vale la pena volver a rastrear; una fecha vieja le dice
"aqui no hay nada nuevo" justo en las paginas que mas nos interesa que relea.

La fecha se toma del ultimo commit que toco el archivo, no de la fecha del
sistema de archivos, que cambia al clonar el repositorio.

Uso
---
  python scripts/sitemap_lastmod.py            # actualiza el sitemap
  python scripts/sitemap_lastmod.py --revisar  # solo informa, no escribe

Se ejecuta solo en cada commit a traves del hook pre-commit.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
RAIZ = Path(__file__).resolve().parent.parent
SITEMAP = RAIZ / "sitemap.xml"
BASE = "https://prunavita.cl"


def ruta_local(url):
    """Traduce una URL del sitemap al archivo que la sirve."""
    camino = url.replace(BASE, "").lstrip("/")
    if camino == "":
        return RAIZ / "index.html"
    if camino == "noticias":
        return RAIZ / "noticias" / "index.html"
    candidato = RAIZ / camino
    if candidato.is_file():
        return candidato
    # URLs sin extension que sirven un index.html
    alterno = RAIZ / camino / "index.html"
    return alterno if alterno.is_file() else None


# Un cambio menor a este numero de lineas se considera retoque, no contenido
# nuevo. Sin este filtro, un reemplazo global (por ejemplo, corregir la ruta del
# logo en todos los archivos) inflaria la fecha de todas las paginas a la vez y
# Google terminaria ignorando el lastmod por poco fiable.
LINEAS_SIGNIFICATIVAS = 10


def fecha_git(archivo):
    """Fecha del ultimo commit con un cambio SUSTANCIAL en el archivo.

    Recorre el historial de mas reciente a mas antiguo y devuelve la fecha del
    primer commit cuyo diff supere el umbral. Si ninguno lo supera, devuelve la
    fecha del commit mas antiguo que toco el archivo (su creacion).
    """
    rel = archivo.relative_to(RAIZ).as_posix()
    r = subprocess.run(
        ["git", "log", "--format=%H %ad", "--date=short", "--numstat", "--", rel],
        capture_output=True, text=True, cwd=RAIZ)
    if not r.stdout.strip():
        return None

    fecha_actual, ultima_vista = None, None
    for linea in r.stdout.splitlines():
        linea = linea.strip()
        if not linea:
            continue
        if re.match(r'^[0-9a-f]{40} \d{4}-\d{2}-\d{2}$', linea):
            fecha_actual = linea.split()[1]
            ultima_vista = fecha_actual
            continue
        partes = linea.split("\t")
        if len(partes) >= 2 and fecha_actual:
            try:
                cambios = int(partes[0]) + int(partes[1])
            except ValueError:      # archivo binario, git marca "-"
                continue
            if cambios >= LINEAS_SIGNIFICATIVAS:
                return fecha_actual
    return ultima_vista


def main():
    ap = argparse.ArgumentParser(description="Sincroniza lastmod del sitemap con git")
    ap.add_argument("--revisar", action="store_true", help="Solo informa; no escribe")
    args = ap.parse_args()

    if not SITEMAP.exists():
        sys.exit("[ERROR] No se encontro sitemap.xml")

    texto = SITEMAP.read_text(encoding="utf-8")
    bloques = re.findall(r'<loc>(.*?)</loc>\s*<lastmod>(\d{4}-\d{2}-\d{2})</lastmod>', texto, re.S)
    if not bloques:
        sys.exit("[ERROR] El sitemap no tiene pares <loc>/<lastmod> reconocibles")

    desfasadas, sin_archivo = [], []
    for url, declarada in bloques:
        archivo = ruta_local(url)
        if archivo is None:
            sin_archivo.append(url)
            continue
        real = fecha_git(archivo)
        if real and real != declarada:
            desfasadas.append((url, declarada, real))

    if sin_archivo:
        print("[AVISO] URLs del sitemap sin archivo local (revisar si sobran):")
        for u in sin_archivo:
            print(f"   {u}")

    if not desfasadas:
        print("[OK] Todas las fechas del sitemap estan al dia.")
        return 0

    print(f"{'ACTUALIZADAS' if not args.revisar else 'DESFASADAS'}: {len(desfasadas)}")
    for url, vieja, nueva in desfasadas:
        print(f"   {url.replace(BASE, '') or '/':<58} {vieja} -> {nueva}")

    if args.revisar:
        return 1

    for url, vieja, nueva in desfasadas:
        patron = re.compile(r'(<loc>' + re.escape(url) + r'</loc>\s*<lastmod>)'
                            + re.escape(vieja) + r'(</lastmod>)')
        texto = patron.sub(lambda m: m.group(1) + nueva + m.group(2), texto, count=1)
    SITEMAP.write_text(texto, encoding="utf-8")
    print(f"\n[OK] sitemap.xml actualizado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
