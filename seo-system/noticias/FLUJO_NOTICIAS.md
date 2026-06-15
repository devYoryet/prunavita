# Flujo Editorial de Noticias — Prunavita.cl

> **DIRECTRIZ DEL CLIENTE (jun 2026):** TODAS las noticias deben ser **investigadas** —buscadas en
> internet, leídas en profundidad, redactadas de forma original por la IA y **vinculadas a lo que es
> Prunavita** (sus servicios y producto). Aunque exista material propio del cliente, debe enriquecerse
> con investigación, datos de fuentes reales y enlaces internos a las páginas de servicio.

Ritmo mensual fijo: **2 noticias investigadas al mes** como mínimo (1 cada 15 días). Si el cliente
aporta material propio, se transforma en una noticia investigada (se contrasta y complementa con
fuentes reales). Todas se publican en `/noticias/` usando `plantilla-noticia.html`.

---

## A) Noticias propias (2/mes — material del cliente)

**Calendario sugerido:** semanas 1 y 3 de cada mes.

1. **Recepción:** el cliente entrega texto bruto, fotos y/o contexto (visita, embarque, feria,
   nuevo cliente, certificación, hito).
2. **Transformación SEO (IA):**
   - Definir keyword objetivo de la nota (ver `KEYWORDS.md`, long-tail).
   - Redactar título periodístico + title SEO ≤ 60 caracteres.
   - Estructura: lead (qué/quién/cuándo) → desarrollo con H2 → cierre con CTA.
   - Mínimo 300 palabras, 2 enlaces internos a páginas de servicio.
3. **Publicación:** duplicar plantilla → completar → quitar `noindex` → tarjeta en
   `/noticias/index.html` → URL en `sitemap.xml` → solicitar indexación en GSC.
4. **Registro:** anotar en la memoria semanal (`memoria/`).

## B) Noticias investigadas (1 cada 15 días — quincenas 2 y 4)

**Flujo obligatorio para la IA (en este orden):**

1. **Buscar fuentes reales en internet** (WebSearch) sobre la temática experta del cliente:
   - mercado mundial/chino de ciruelas deshidratadas y fruta deshidratada
   - exportaciones agroindustriales chilenas (cifras ODEPA, ProChile, Aduanas)
   - normativa de inocuidad y requisitos de mercados (GACC, UE, FDA)
   - tecnología y maquinaria de procesamiento
2. **Leer el contenido completo** de 1–3 fuentes (WebFetch), no solo titulares.
3. **Extraer ideas y datos relevantes:** cifras, fechas, actores, tendencia. No inventar datos.
4. **Redactar noticia ORIGINAL** con enfoque experto:
   - No traducir ni parafrasear de cerca: sintetizar con ángulo propio para el lector B2B.
   - Incluir sección final **"La mirada de Prunavita"** con análisis propio del equipo
     y enlace a la página de servicio relacionada.
   - Citar la fuente con enlace (`rel="noopener nofollow"`).
5. **Optimizar para SEO:** keyword long-tail en title, H1, primer párrafo y description.
6. **Publicar o dejar lista** (si requiere visto bueno del cliente, dejarla con `noindex`
   y avisar; quitar `noindex` al aprobar).

### Prompt operativo para cada noticia investigada

```
Lee seo-system/PROMPT_MAESTRO.md y la última memoria semanal. Toca noticia investigada
de la quincena. 1) Busca en internet 3 noticias recientes sobre [tema del calendario].
2) Elige la más relevante para compradores/exportadores agroindustriales, lee la fuente
completa y extrae los datos. 3) Redacta una noticia original de 400-600 palabras con la
estructura de /noticias/plantilla-noticia.html, sección "La mirada de Prunavita" y enlace
al servicio relacionado. 4) Publícala (quitar noindex, tarjeta en /noticias/, sitemap.xml).
5) Registra todo en la memoria semanal.
```

## Calendario editorial tipo (cada mes)

| Semana | Contenido | Responsable inicia |
|---|---|---|
| 1 | Noticia propia #1 | Cliente entrega material |
| 2 | Noticia investigada #1 | IA (búsqueda real) |
| 3 | Noticia propia #2 | Cliente entrega material |
| 4 | Noticia investigada #2 | IA (búsqueda real) |

## Temas pre-aprobados para noticias investigadas (rotar)

1. Temporada/precios de la ciruela deshidratada chilena (fuentes: ODEPA, Chileprunes, portales agro).
2. Mercado chino/asiático de frutos secos y fruta deshidratada.
3. Acuerdos comerciales y requisitos de exportación (SAG, GACC, UE).
4. Tendencias de consumo de snacks saludables.
5. Innovación en procesamiento y maquinaria agroindustrial.
6. Logística y fletes marítimos Chile-Asia.

## Convención de nombres de archivo

`/noticias/AAAA-MM-slug-corto.html` — ej.: `2026-07-china-importaciones-ciruela.html`
