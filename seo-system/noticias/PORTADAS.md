# Registro de portadas — noticias Prunavita.cl

> Mantenido con `scripts/portada_noticia.py`.
> **Regla dura: una imagen no puede aparecer en dos noticias.** Ni como portada de una y
> foto interior de otra. Cada noticia lleva 2 imágenes propias (portada + interior).

Verificación automática antes de publicar:

```bash
python scripts/portada_noticia.py auditar
```

Falla con código de salida 1 si alguna imagen se repite entre noticias.

---

## Asignación vigente

| Noticia (slug) | Portada (hero + og:image + tarjeta) | Foto interior | Fuente |
|---|---|---|---|
| `2026-07-ciruela-deshidratada-chile-certificacion-sustentable-apl` | `huerto-ciruelos.jpg` | `linea-produccion-fruta.jpg` | Pexels #30560206 / #11679691 |
| `2026-07-requisitos-exportar-ciruela-deshidratada-china-gacc` | `export-container.jpg` | `quality-control.jpg` | banco original |
| `2026-07-exportacion-ciruela-deshidratada-mercados-2026` | `dried-fruit-market.jpg` | `global-export.jpg` | banco original |
| `2026-06-exportacion-ciruela-deshidratada-chile-2025` | `puerto-contenedores.jpg` | `ciruelas-arbol.jpg` | Pexels #32399137 / #13144689 |
| `2026-06-prunavita-clientes-vina-santa-rita` | `linkedin-vina-1.jpg` | `linkedin-vina-2.jpg` | fotos propias del cliente |

Hub `/noticias/` (no es noticia): `hero-prunes.jpg` como og:image y fondo de cabecera.

## Imágenes libres (no asignadas a ninguna noticia)

Disponibles para la próxima nota, pero **cada una se puede usar una sola vez**:

| Archivo | Qué muestra |
|---|---|
| `prunes-close.jpg` | Primer plano de ciruelas deshidratadas a granel |
| `linkedin-vina-3.jpg` | Visita a Viña Santa Rita, tercera toma |
| `machinery.jpg` / `maquinaria.jpg` | Maquinaria agroindustrial |
| `team-business.jpg` | Equipo comercial en reunión |

> Ojo: `hero-prunes.jpg` está tomada por el hub. `prunes-close.jpg` y `hero-prunes.jpg`
> se parecen mucho entre sí — no las uses en noticias contiguas.

---

## Cómo conseguir una portada nueva

**1 — Stock real (opción por defecto).** Fotos reales, licencia comercial libre, sin costo.
Coherente con la directriz del cliente de que el contenido sea real.

```bash
python scripts/portada_noticia.py buscar "dried fruit processing plant"
python scripts/portada_noticia.py usar --id 11679691 \
    --slug 2026-08-mi-noticia --nombre linea-secado \
    --descripcion "Linea de secado de fruta en planta agroindustrial"
```

Requiere `PEXELS_API_KEY` (gratis en <https://www.pexels.com/api/>) en `.env`.
La foto se descarga ya recortada a **1600x900**, el formato de portada del sitio.

**2 — Generación con IA (excepción).** Solo cuando no existe foto real adecuada:
mapas de destinos, esquemas de proceso, gráficos de mercado, conceptos abstractos.

```bash
python scripts/portada_noticia.py generar \
    --slug 2026-08-mi-noticia --nombre mapa-destinos \
    --prompt "Mapa editorial de rutas de exportacion Chile-Asia, estilo plano, tonos verdes"
```

Requiere `OPENAI_API_KEY` en `.env`. Costo aproximado US$0,17 por imagen en calidad alta.

**Nunca generes con IA** fotos que simulen ser reales: planta, fruta, personas, instalaciones.
El cliente exige contenido real y una foto de IA que aparente ser una planta de Prunavita
es exactamente lo que pidió no hacer.

## Criterios de una buena portada

- **Distinta a simple vista** de las 3 noticias anteriores. No basta con que sea otro archivo:
  dos primeros planos de ciruelas oscuras se leen como la misma foto. Alterna registros —
  campo, planta, puerto, laboratorio, producto, personas.
- **Horizontal 16:9**, mínimo 1600x900.
- **Bajo 400 KB.** El recorte de Pexels ya entrega ese rango.
- **Relacionada con el ángulo de la nota**, no solo con el rubro.
- **`alt` que describa lo que la foto muestra de verdad**, con la keyword si calza natural.
  Si la foto es un puerto, el alt habla de un puerto — no de ciruelas.
| `2026-08-reglamento-sanitario-alimentos-chile-exportadores` | `laboratorio-analisis-alimentos.jpg` | Pexels #3735781 | Analisis de laboratorio en control de inocuidad alimentaria |
| `2026-08-reglamento-sanitario-alimentos-chile-exportadores` | `planta-procesamiento-alimentos.jpg` | Pexels #2889193 | Procesamiento de alimentos en planta industrial (foto interior) |
| `2026-08-maquinaria-agroindustrial-usada-que-revisar` | `tecnico-tablero-maquinaria.jpg` | Pexels #35072831 | Tecnico interviniendo tablero de control de maquina industrial |
