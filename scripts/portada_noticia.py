#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Portadas de noticias — Prunavita.cl

Garantiza que CADA noticia publicada tenga una foto de portada unica.
Estrategia hibrida:
  1. Stock real (Pexels)  -> por defecto. Fotos reales, licencia libre.
  2. Generacion (OpenAI)  -> solo si no existe stock adecuado (infografias,
     mapas de destinos, conceptos sin equivalente fotografico).

El registro seo-system/noticias/PORTADAS.md es la fuente de verdad:
el script se niega a reutilizar una imagen ya asignada a otra noticia.

Uso
---
  # Buscar stock real y ver candidatos (no descarga nada)
  python scripts/portada_noticia.py buscar "plum orchard harvest"

  # Descargar un candidato y asignarlo a una noticia
  python scripts/portada_noticia.py usar --id 30560206 \
      --slug 2026-08-mi-noticia --nombre huerto-atardecer

  # Generar con OpenAI cuando no hay stock adecuado
  python scripts/portada_noticia.py generar \
      --slug 2026-08-mi-noticia --nombre mapa-destinos \
      --prompt "Mapa isometrico de rutas de exportacion Chile-Asia, estilo editorial"

  # Auditar: detecta portadas repetidas entre noticias
  python scripts/portada_noticia.py auditar

Claves (en .env en la raiz del proyecto, NUNCA en el repositorio):
  PEXELS_API_KEY=...   (gratis en pexels.com/api — solo para 'buscar')
  OPENAI_API_KEY=...   (solo para 'generar')
"""

import argparse
import base64
import hashlib
import os
import re
import sys
from pathlib import Path

import requests

RAIZ = Path(__file__).resolve().parent.parent
DIR_IMAGENES = RAIZ / "assets" / "images"
REGISTRO = RAIZ / "seo-system" / "noticias" / "PORTADAS.md"
DIR_NOTICIAS = RAIZ / "noticias"

# Formato de portada del sitio (tarjeta del hub + hero + og:image)
ANCHO, ALTO = 1600, 900


# --------------------------------------------------------------------------
# Utilidades
# --------------------------------------------------------------------------

def cargar_env():
    """Lee .env de la raiz sin dependencias externas."""
    ruta = RAIZ / ".env"
    if not ruta.exists():
        return
    for linea in ruta.read_text(encoding="utf-8").splitlines():
        linea = linea.strip()
        if not linea or linea.startswith("#") or "=" not in linea:
            continue
        clave, valor = linea.split("=", 1)
        os.environ.setdefault(clave.strip(), valor.strip().strip('"').strip("'"))


def exigir_clave(nombre):
    valor = os.environ.get(nombre)
    if not valor:
        sys.exit(
            f"[ERROR] Falta {nombre}.\n"
            f"        Agregala en {RAIZ / '.env'} (ese archivo esta en .gitignore).\n"
            f"        Ejemplo:  {nombre}=tu-clave-aqui"
        )
    return valor


# Assets de plantilla (nav, footer) que legitimamente se repiten en toda noticia.
CHROME = re.compile(r"logo|favicon|icon", re.IGNORECASE)


def imagenes_en_uso():
    """Devuelve {nombre_archivo: [noticias que la usan]} leyendo el HTML real.

    Excluye los assets de plantilla (logos, iconos): esos deben repetirse.
    """
    uso = {}
    for html in sorted(DIR_NOTICIAS.glob("*.html")):
        if html.name in ("plantilla-noticia.html", "index.html"):
            continue
        texto = html.read_text(encoding="utf-8", errors="ignore")
        for archivo in set(re.findall(r"assets/images/([A-Za-z0-9_-]+\.(?:jpg|jpeg|png|webp))", texto)):
            if CHROME.search(archivo):
                continue
            uso.setdefault(archivo, []).append(html.name)
    return uso


def hash_archivo(ruta):
    return hashlib.sha256(ruta.read_bytes()).hexdigest()[:16]


def guardar(contenido, nombre):
    destino = DIR_IMAGENES / f"{nombre}.jpg"
    if destino.exists():
        sys.exit(f"[ERROR] Ya existe {destino.name}. Elige otro --nombre.")

    firma = hashlib.sha256(contenido).hexdigest()[:16]
    for existente in DIR_IMAGENES.glob("*.jpg"):
        if hash_archivo(existente) == firma:
            sys.exit(
                f"[ERROR] Esa foto ya esta en el banco como {existente.name}. "
                f"Es un duplicado exacto — busca otra."
            )

    destino.write_bytes(contenido)
    print(f"[OK] Guardada: assets/images/{destino.name}  ({len(contenido) // 1024} KB)")
    return destino


def registrar(slug, nombre_archivo, fuente, descripcion):
    """Anexa la portada al registro PORTADAS.md."""
    REGISTRO.parent.mkdir(parents=True, exist_ok=True)
    if not REGISTRO.exists():
        REGISTRO.write_text(
            "# Registro de portadas — noticias Prunavita.cl\n\n"
            "> Generado y mantenido por `scripts/portada_noticia.py`.\n"
            "> **Regla: una imagen no puede aparecer en dos noticias.**\n\n"
            "| Noticia (slug) | Imagen | Fuente | Descripcion |\n"
            "|---|---|---|---|\n",
            encoding="utf-8",
        )
    with REGISTRO.open("a", encoding="utf-8") as fh:
        fh.write(f"| `{slug}` | `{nombre_archivo}` | {fuente} | {descripcion} |\n")
    print(f"[OK] Registrada en {REGISTRO.relative_to(RAIZ)}")


# --------------------------------------------------------------------------
# Comandos
# --------------------------------------------------------------------------

def cmd_buscar(args):
    cargar_env()
    clave = exigir_clave("PEXELS_API_KEY")

    resp = requests.get(
        "https://api.pexels.com/v1/search",
        headers={"Authorization": clave},
        params={"query": args.consulta, "per_page": args.cantidad, "orientation": "landscape"},
        timeout=30,
    )
    resp.raise_for_status()
    fotos = resp.json().get("photos", [])

    if not fotos:
        print(f"Sin resultados para: {args.consulta}")
        return

    en_uso = imagenes_en_uso()
    print(f"\n{len(fotos)} candidatos para «{args.consulta}»:\n")
    for foto in fotos:
        print(f"  id {foto['id']:<12} {foto['width']}x{foto['height']}  por {foto['photographer']}")
        print(f"     {foto['url']}")
        print(f"     preview: {foto['src']['medium']}")
    print(
        f"\nBanco actual: {len(en_uso)} imagenes ya asignadas a noticias."
        f"\nSiguiente paso:\n"
        f"  python scripts/portada_noticia.py usar --id <ID> --slug <slug> --nombre <nombre-archivo>\n"
    )


def cmd_usar(args):
    url = (
        f"https://images.pexels.com/photos/{args.id}/pexels-photo-{args.id}.jpeg"
        f"?auto=compress&cs=tinysrgb&w={ANCHO}&h={ALTO}&fit=crop"
    )
    print(f"Descargando Pexels #{args.id} recortada a {ANCHO}x{ALTO}...")
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    if not resp.content.startswith(b"\xff\xd8"):
        sys.exit(f"[ERROR] La respuesta no es un JPEG valido. Verifica el id {args.id}.")

    destino = guardar(resp.content, args.nombre)
    registrar(
        args.slug,
        destino.name,
        f"Pexels #{args.id}",
        args.descripcion or "(completar)",
    )
    recordatorio(args.slug, destino.name)


def cmd_generar(args):
    cargar_env()
    clave = exigir_clave("OPENAI_API_KEY")

    print("Generando con OpenAI (gpt-image-1)... puede tardar ~30 s")
    resp = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers={"Authorization": f"Bearer {clave}", "Content-Type": "application/json"},
        json={
            "model": "gpt-image-1",
            "prompt": args.prompt,
            "size": "1536x1024",
            "quality": "high",
            "n": 1,
        },
        timeout=180,
    )
    if resp.status_code != 200:
        sys.exit(f"[ERROR] OpenAI {resp.status_code}: {resp.text[:500]}")

    datos = resp.json()["data"][0]
    contenido = base64.b64decode(datos["b64_json"]) if "b64_json" in datos else requests.get(datos["url"], timeout=60).content

    destino = guardar(contenido, args.nombre)
    registrar(args.slug, destino.name, "OpenAI gpt-image-1", args.prompt[:90])
    print("\n[AVISO] Imagen generada por IA. Segun la directriz del cliente, usala solo\n"
          "        para conceptos sin equivalente fotografico (mapas, esquemas, graficos).\n"
          "        Nunca para simular fotos reales de planta, fruta o personas.")
    recordatorio(args.slug, destino.name)


def cmd_auditar(args):
    uso = imagenes_en_uso()
    repetidas = {img: notas for img, notas in uso.items() if len(notas) > 1}

    print(f"\nImagenes en uso por noticias: {len(uso)}")
    if repetidas:
        print("\n[FALLA] Imagenes compartidas por mas de una noticia:\n")
        for img, notas in sorted(repetidas.items()):
            print(f"  {img}")
            for nota in sorted(notas):
                print(f"      - {nota}")
        print("\nCada noticia debe tener portada propia. Corrige antes de publicar.")
        sys.exit(1)

    print("[OK] Ninguna imagen se repite entre noticias.\n")
    for img, notas in sorted(uso.items()):
        print(f"  {img:<38} {notas[0]}")


def recordatorio(slug, nombre_archivo):
    print(
        f"\nFalta actualizar a mano en la noticia y en el hub:\n"
        f"  1. noticias/{slug}.html  ->  og:image, JSON-LD \"image\", .page-hero-bg\n"
        f"  2. noticias/index.html   ->  <img> de la tarjeta\n"
        f"  Ruta: ../assets/images/{nombre_archivo}\n"
        f"  Recuerda escribir un alt descriptivo REAL de lo que muestra la foto.\n"
        f"  Verifica al final con:  python scripts/portada_noticia.py auditar"
    )


def main():
    parser = argparse.ArgumentParser(description="Portadas unicas para noticias de Prunavita.cl")
    sub = parser.add_subparsers(dest="comando", required=True)

    p = sub.add_parser("buscar", help="Buscar fotos de stock reales en Pexels")
    p.add_argument("consulta", help="Consulta en ingles, ej: 'plum orchard harvest'")
    p.add_argument("--cantidad", type=int, default=8)
    p.set_defaults(func=cmd_buscar)

    p = sub.add_parser("usar", help="Descargar un candidato de Pexels y registrarlo")
    p.add_argument("--id", required=True, help="ID de la foto en Pexels")
    p.add_argument("--slug", required=True, help="Slug de la noticia, ej: 2026-08-mi-noticia")
    p.add_argument("--nombre", required=True, help="Nombre del archivo sin extension")
    p.add_argument("--descripcion", help="Que muestra la foto (para el registro)")
    p.set_defaults(func=cmd_usar)

    p = sub.add_parser("generar", help="Generar con OpenAI (solo si no hay stock adecuado)")
    p.add_argument("--slug", required=True)
    p.add_argument("--nombre", required=True)
    p.add_argument("--prompt", required=True)
    p.set_defaults(func=cmd_generar)

    p = sub.add_parser("auditar", help="Verificar que ninguna noticia repita portada")
    p.set_defaults(func=cmd_auditar)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
