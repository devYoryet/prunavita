# Plan de palancas — Prunavita.cl

**Creado:** 3 de agosto de 2026 · **Vigencia:** agosto–noviembre 2026
**Métrica norte:** clics desde búsquedas **no-marca**. Línea base: **0**.

> Todo el tráfico actual (20 clics/28 días) viene de gente que busca "prunavita" por su
> nombre. El proyecto no habrá funcionado hasta que lleguen clics de gente que **no** conocía
> a la empresa. Esa es la única métrica que decide si las palancas sirven.

## Línea base — 3 de agosto de 2026

| Indicador | Valor |
|---|---|
| Clics totales (28 d) | 20 |
| Impresiones (28 d) | 113 |
| Posición media | 11,9 |
| Consultas reveladas (90 d) | 7 |
| Páginas con impresiones | 12 |
| **Clics no-marca** | **0** |

Registrado en `seguimiento/historico.csv`. Se actualiza con `scripts/seguimiento_seo.py foto`.

---

## Las palancas, por retorno esperado

Ordenadas por impacto sobre la métrica norte, no por facilidad.

### A · Contenido — el mayor impacto, el más lento

| # | Palanca | Estado | Detalle |
|---|---|---|---|
| A1 | **Profundizar páginas de servicio** | Pendiente | 525–725 → ~1.800 palabras. Orden: Asesorías (4 de 7 consultas reveladas) → Ciruelas (más impresiones) → Maquinaria → Exportación → Representación |
| A2 | **2 noticias/mes dirigidas** | En curso | Ya no noticias sueltas del sector: cada una ataca un término comercial detectado y enlaza a su página de servicio |
| A3 | **Clusters de enlace interno** | Pendiente | Cada noticia enlaza a la página de servicio de su tema. Hoy los enlaces son genéricos |
| A4 | **FAQ con datos estructurados** | Pendiente | `FAQPage` en cada página de servicio. Captura búsquedas en forma de pregunta y puede ganar espacio ampliado en resultados |
| A5 | **Página pilar de exportación** | Mes 4 | Guía extensa que concentre autoridad temática y reciba enlaces desde las noticias |

### B · Técnico — rápido de ejecutar, efecto acotado

| # | Palanca | Estado | Detalle |
|---|---|---|---|
| B1 | **Borrar imágenes huérfanas** | Pendiente | 17 MB en la raíz (`team-business.jpg` 13,2 MB, `global-export.jpg`, `quality-control.jpg`) que **ningún HTML referencia**. No afectan velocidad; sí ensucian el deploy |
| B2 | **Logo de datos estructurados** | Pendiente | `logo_prunavita.png` pesa 2,3 MB y se declara como logo de la organización en el JSON-LD de 7 páginas. Debe bajar de 100 KB |
| B3 | **Imágenes a WebP** | Pendiente | Las portadas nuevas ya vienen a 1600×900; falta convertir el banco antiguo |
| B4 | **Schema `Service` y `BreadcrumbList`** | Pendiente | Las páginas de servicio no declaran su tipo. Ayuda a que Google entienda qué se ofrece |
| B5 | **Noticia GACC sin impresiones** | Pendiente | Publicada hace 3 semanas, cero impresiones mientras las otras 4 sí aparecen. Requiere inspección de URL en GSC |
| B6 | **Indexación tras publicar** | Continuo | Enviar cada URL nueva a inspección en GSC el mismo día |

### C · Autoridad — lento, y sin esto hay techo

> **Se adelanta desde septiembre a agosto.** El plan original los ponía en los meses 4–5.
> Los enlaces tardan meses en rendir; empezar en septiembre significa cosechar en diciembre,
> cuando el contrato ya terminó.

| # | Palanca | Estado | Requiere del cliente |
|---|---|---|---|
| C1 | **Google Business Profile** | Pendiente | Validación por correo o teléfono |
| C2 | **ProChile** — directorio exportadores | Pendiente | Datos de empresa y RUT |
| C3 | **Chilealimentos** | Pendiente | Confirmar si son socios |
| C4 | **Chileprunes** — gremio del rubro | Pendiente | Confirmar membresía |
| C5 | **Alibaba / Made-in-China** | Pendiente | Cuenta B2B. Doble beneficio: enlace + canal China |
| C6 | **LinkedIn de empresa** | Pendiente | Acceso a la página |

### D · Medición — sin esto no se sabe si algo funcionó

| # | Palanca | Estado | Detalle |
|---|---|---|---|
| D1 | **Seguimiento diario** | ✅ Operativo | `scripts/seguimiento_seo.py` acumula el histórico |
| D2 | **Separar marca / no-marca** | ✅ Operativo | Integrado en el script y en los reportes |
| D3 | **Desbloquear GA4** | Pendiente | Habilitar Analytics Admin/Data API + rol Lector para la cuenta de servicio |
| D4 | **Bing Webmaster Tools** | Pendiente | Tráfico menor, pero es gratis y alimenta a ChatGPT/Copilot |

### E · Internacional — meses 4–5

| # | Palanca | Estado |
|---|---|---|
| E1 | **Baidu Webmaster + `/zh`** | Página creada, registro pendiente (requiere cuenta Baidu) |
| E2 | **Versión en inglés** | Justificada por las impresiones desde EE.UU. sin clics |

---

## Secuencia

**Agosto — atacar lo que ya muestra intención comercial**
1. Ampliar Asesorías en inocuidad (A1)
2. Ampliar Ciruelas deshidratadas (A1)
3. Limpieza técnica B1 + B2 (una tarde de trabajo)
4. Iniciar altas de autoridad C1–C5
5. 2 noticias dirigidas a BRC y maquinaria usada (A2 + A3)
6. Desbloquear GA4 (D3)

**Septiembre — profundizar y medir el efecto**
- Ampliar Maquinaria y Exportación (A1)
- FAQ con schema en las páginas ya ampliadas (A4)
- Primera lectura del efecto de agosto sobre posiciones
- 2 noticias + reporte mensual

**Octubre–noviembre — consolidar y abrir China**
- Página pilar (A5), Baidu (E1), evaluación de versión EN (E2)
- Informe final con la serie completa del histórico

---

## Cadencia de seguimiento

| Cuándo | Qué | Comando |
|---|---|---|
| **Diario** | Foto del día al histórico | `python scripts/seguimiento_seo.py foto` |
| **Lunes** | Revisar tendencia y posiciones objetivo | `python scripts/seguimiento_seo.py todo` |
| **Fin de mes** | Reporte al cliente | Manual, sobre el histórico acumulado |

> Search Console tiene **2–3 días de retraso** y las posiciones se mueven en semanas, no en
> horas. La foto diaria sirve para **acumular la serie**, no para reaccionar cada día. La
> decisión se toma los lunes; mirar el dato a diario solo genera ruido.

## Cómo se sabrá si funcionó

| Hito | Plazo | Estado |
|---|---|---|
| Primer clic **no-marca** | Sep 2026 | ⬜ 0 hoy |
| 40–60 consultas reveladas | Sep 2026 | ⬜ 7 hoy |
| Keywords objetivo en rango 15–25 | Oct 2026 | ⬜ 29–80 hoy |
| Primera keyword comercial en página 1 | Nov 2026 | ⬜ ninguna |

**Lo que no se promete:** una posición concreta en una fecha concreta. Llevar una consulta de
la posición 60 a la primera página toma de 3 a 6 meses con contenido y autoridad. Cualquier
promesa más precisa que eso es adivinanza.
