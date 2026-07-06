# Guía de medición SEO — Prunavita.cl

**Para:** Cliente (Felipe / equipo Prunavita) y mantención mensual  
**Actualizado:** 6 de julio de 2026 · Mes 2 del plan  
**Sitio:** https://prunavita.cl

---

## 1. Respuesta corta: ¿ya sale en Google?

**El sitio está publicado y configurado para SEO, pero el posicionamiento visible en Google aún está en fase inicial (mes 2).**

| Tipo de búsqueda | Ejemplo | Situación jul 2026 |
|---|---|---|
| **Marca** | `prunavita` | Por confirmar en Search Console |
| **Marca + servicio** | `prunavita ciruelas deshidratadas` | **Sin posición visible en Google** (predominan otros sitios del sector) |
| **Genérica sin marca** | `exportador ciruelas deshidratadas Chile` | No esperado en mes 2 |

**Indexación:** confirmar en Google Search Console cuántas de las 13 URLs del sitemap están indexadas. No asumir posiciones sin datos de GSC o búsqueda manual documentada.

> El SEO orgánico tarda **6–12 semanas** en mostrar resultados después de publicar páginas nuevas. La medición formal comienza en la 2ª semana de julio.

---

## 2. Cómo comprobarlo ustedes mismos (5 minutos)

### A) Google Search Console (la fuente oficial)

1. Entrar a https://search.google.com/search-console  
2. Propiedad: `prunavita.cl` (debe estar verificada)  
3. Revisar:

| Sección | Qué mirar |
|---|---|
| **Páginas** → Indexación | Cuántas URLs están indexadas (meta mes 2: 10–13) |
| **Rendimiento** | Impresiones, clics, CTR, posición media (primeros datos en 2–4 semanas) |
| **Sitemaps** | `sitemap.xml` enviado y sin errores |
| **Inspección de URLs** | Pegar una URL → "La URL está en Google" |

**URLs a inspeccionar una por una:**
```
https://prunavita.cl/
https://prunavita.cl/servicios/ciruelas-deshidratadas.html
https://prunavita.cl/servicios/exportacion-agroindustrial.html
https://prunavita.cl/noticias/
https://prunavita.cl/fichas-tecnicas.html
```

### B) Búsqueda manual en Google (modo incógnito)

Probar estas búsquedas y anotar en qué posición aparece `prunavita.cl`:

1. `prunavita`
2. `prunavita ciruelas deshidratadas`
3. `prunavita exportación agroindustrial`
4. `site:prunavita.cl` → lista todas las páginas que Google tiene indexadas

### C) Google Analytics 4

1. https://analytics.google.com → propiedad `G-0G9GQYN4RE`  
2. **Informes** → **Adquisición** → **Adquisición de tráfico**  
3. Filtrar canal = **Organic Search**  
4. Ver páginas de entrada y sesiones desde Google

---

## 3. Estado a documentar (baseline julio 2026)

Registrar en el primer reporte mensual — **solo con datos verificados** (GSC o búsqueda manual):

| URL | Indexada en Google (GSC) |
|---|---|
| `/` | [completar] |
| `/servicios/ciruelas-deshidratadas.html` | [completar] |
| `/servicios/exportacion-agroindustrial.html` | [completar] |
| `/noticias/` | [completar] |
| `/fichas-tecnicas.html` | [completar] |

### Búsquedas a registrar (posición real en Google, modo incógnito)

| Búsqueda | Posición prunavita.cl | Fecha |
|---|---|---|
| `prunavita` | [completar] | |
| `prunavita ciruelas deshidratadas` | [completar] | |
| `site:prunavita.cl` | [nº páginas indexadas] | |

### Búsquedas genéricas — expectativa mes 2

| Búsqueda | Estado esperado |
|---|---|
| `exportador ciruelas deshidratadas Chile` | Sin posición en primera página |
| `gestión exportaciones agroindustrial Chile` | Sin posición en primera página |

**Objetivo mes 3–6:** entrar al top 50, luego top 20, luego top 10 en 2–3 keywords por página pilar.

---

## 4. Plan de medición y reportes al cliente

### Calendario acordado

| Hito | Fecha |
|---|---|
| **Inicio medición formal** | Segunda semana de julio 2026 (desde ~14 jul) |
| **Frecuencia de reporte al cliente** | **1 vez al mes** (cierre de cada mes) |
| **Primer reporte mensual** | Finales de julio / primeros días de agosto 2026 |
| **Registro interno** | Semanal en `memoria/` (uso operativo del consultor) |

> La Etapa 1 (jun–6 jul) fue implementación intensiva. La medición con baseline en Search Console
> comienza cuando Google haya tenido tiempo de indexar; por eso el primer reporte con datos comparables
> sale a fin de mes, no antes.

### Contenido de cada reporte mensual

Ver plantilla: `PLANTILLA_REPORTE_MENSUAL.md`

1. Resumen ejecutivo (3–5 líneas)
2. KPIs: indexadas, impresiones, clics, CTR, posición media
3. Tabla de keywords y posiciones
4. Publicaciones del mes (2)
5. Trabajos técnicos realizados
6. Recomendaciones mes siguiente

---

## 5. KPIs mensuales (mantención SEO)

Cada mes (día 1 o al cierre del informe) registrar en `memoria/YYYY-MM.md`:

### KPIs obligatorios

| KPI | Fuente | Meta mes 3 | Meta mes 6 |
|---|---|---|---|
| Páginas indexadas | GSC → Páginas | 13+ | 20+ |
| Impresiones orgánicas/mes | GSC → Rendimiento | 500+ | 3.000+ |
| Clics orgánicos/mes | GSC → Rendimiento | 30+ | 150+ |
| CTR medio | GSC | > 2% | > 3% |
| Posición media | GSC | < 40 | < 25 |
| Keywords en top 10 | GSC + manual | 2 | 8 |
| Sesiones orgánicas | GA4 | 50+ | 300+ |

### Keywords a seguir (copiar tabla cada mes)

| Keyword | Página objetivo | Posición mes anterior | Posición actual | Impresiones | Clics |
|---|---|---|---|---|---|
| prunavita | / | | | | |
| ciruelas deshidratadas Chile | /servicios/ciruelas-deshidratadas.html | | | | |
| exportador ciruelas deshidratadas | /servicios/ciruelas-deshidratadas.html | | | | |
| gestión exportaciones Chile | /servicios/exportacion-agroindustrial.html | | | | |
| representación comercial Chile | /servicios/representacion-comercial.html | | | | |
| maquinaria agroindustrial Chile | /servicios/maquinaria-agroindustrial.html | | | | |
| asesoría HACCP Chile | /servicios/asesorias-tecnicas-inocuidad.html | | | | |

### Acciones de mantención según datos

| Señal en GSC | Acción |
|---|---|
| URL no indexada tras 2 semanas | Inspección → Solicitar indexación + revisar enlaces internos |
| Impresiones pero 0 clics (CTR < 1%) | Mejorar title y meta description |
| Posición 8–20 | Reforzar contenido de la página + enlaces desde noticias |
| Posición > 50 | Publicar noticia long-tail que enlace a la página pilar |
| Nueva keyword en GSC | Agregar a KEYWORDS.md y crear/ajustar contenido |

---

## 6. Qué decirle al cliente (mensaje tipo)

> El sitio tiene la **base técnica lista** para posicionar. Los resultados en Google se medirán mes a mes
> con Search Console y se reportarán sin suposiciones. En mes 2 es normal no aparecer aún en búsquedas
> competitivas como "prunavita ciruelas deshidratadas".

---

## 7. Próximas acciones técnicas (julio 2026)

- [ ] Confirmar en GSC cuántas de las 13 URLs del sitemap están indexadas
- [ ] Solicitar indexación manual de URLs pendientes
- [ ] Revisar GSC → Rendimiento → Consultas (primeras keywords reales)
- [ ] Registrar baseline de julio en `memoria/2026-07-S1.md`
- [ ] 2 publicaciones julio según plan editorial
- [ ] Ajustar titles/descriptions si CTR bajo en páginas con impresiones

---

## 8. Herramientas recomendadas

| Herramienta | Uso | Costo |
|---|---|---|
| Google Search Console | Indexación, keywords, clics | Gratis |
| Google Analytics 4 | Tráfico y conversiones | Gratis |
| Bing Webmaster Tools | Indexación Bing (opcional) | Gratis |
| PageSpeed Insights | Velocidad / Core Web Vitals | Gratis |
| Ubersuggest / Semrush | Seguimiento posiciones (opcional) | Pago |

Para esta etapa, **GSC + GA4 son suficientes**.
