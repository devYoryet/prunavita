# Plan de palancas — Prunavita.cl

**Creado:** 3 de agosto de 2026 · **Vigencia:** agosto–noviembre 2026
**Métrica norte:** **clics a páginas interiores** (los que no caen en la home).
Línea base: **11** de 20 el 3 de agosto de 2026.

> El objetivo del proyecto es traer gente que **no** conocía a la empresa. Quien busca
> "prunavita" por su nombre aterriza en la home; quien entra a una página de servicio o a
> una noticia venía buscando otra cosa. Por eso el reparto de clics entre home e interiores
> es el termómetro: cuando suben los interiores, están llegando búsquedas de necesidad.

> **Por qué no se mide por consulta.** Hasta el 10 de agosto la métrica norte era "clics
> desde consultas no-marca", y daba 0 semana tras semana. No era el sitio: Google oculta las
> consultas de bajo volumen y en este sitio esas son hoy el **100%** de los clics, así que
> la métrica daba 0 por construcción, sin importar cómo fuera el sitio realmente. La columna
> `clics_no_marca` se conserva en el histórico por si el volumen crece y vuelve a distinguir.

## Línea base — 3 de agosto de 2026

| Indicador | Valor |
|---|---|
| Clics totales (28 d) | 20 |
| Impresiones (28 d) | 113 |
| Posición media | 11,9 |
| Consultas reveladas (28 d) | 7 |
| Páginas con impresiones | 12 |
| **Clics a páginas interiores** | **11** |

Registrado en `seguimiento/historico.csv`. Se actualiza con `scripts/seguimiento_seo.py foto`.

> Los valores de la métrica norte anteriores al 10 de agosto se reconstruyeron con datos ya
> consolidados; las fotos del día se toman con los últimos 2–3 días aún incompletos, así que
> pueden quedar 1–2 clics por debajo. Sirve para la tendencia, no para el decimal.

---

## Las palancas, por retorno esperado

Ordenadas por impacto sobre la métrica norte, no por facilidad.

### A · Contenido — el mayor impacto, el más lento

| # | Palanca | Estado | Detalle |
|---|---|---|---|
| A1 | **Profundizar páginas de servicio** | ✅ Completo (ago 2026) | Las cinco ampliadas: Asesorías 588→1.771, Ciruelas 725→1.457, Maquinaria 562→1.363, Exportación 470→1.213, Representación 418→1.016 |
| A2 | **2 noticias/mes dirigidas** | En curso | Ya no noticias sueltas del sector: cada una ataca un término comercial detectado y enlaza a su página de servicio |
| A3 | **Clusters de enlace interno** | 🔸 Media vuelta | Noticia → servicio: hecho, las 7 noticias enlazan desde el cuerpo a la página de su tema (además de los 5 del pie). Falta el sentido inverso: Asesorías y Exportación no enlazan a ninguna noticia, Maquinaria y Representación solo a una |
| A4 | **FAQ con datos estructurados** | Pendiente | `FAQPage` en cada página de servicio. Captura búsquedas en forma de pregunta y puede ganar espacio ampliado en resultados |
| A5 | **Página pilar de exportación** | Mes 4 | Guía extensa que concentre autoridad temática y reciba enlaces desde las noticias |

### B · Técnico — rápido de ejecutar, efecto acotado

| # | Palanca | Estado | Detalle |
|---|---|---|---|
| B1 | **Borrar imágenes huérfanas** | ✅ Hecho | 17 MB en la raíz (`team-business.jpg` 13,2 MB, `global-export.jpg`, `quality-control.jpg`) que **ningún HTML referencia**. No afectan velocidad; sí ensucian el deploy |
| B2 | **Logo de datos estructurados** | ✅ Hecho (2.290→118 KB) | `logo_prunavita.png` pesa 2,3 MB y se declara como logo de la organización en el JSON-LD de 7 páginas. Debe bajar de 100 KB |
| B3 | **Imágenes a WebP** | Pendiente | Las portadas nuevas ya vienen a 1600×900; falta convertir el banco antiguo |
| B4 | **Schema `Service` y `BreadcrumbList`** | Pendiente | Las páginas de servicio no declaran su tipo. Ayuda a que Google entienda qué se ofrece |
| B5 | **Noticia GACC sin impresiones** | 🔎 Diagnosticado | **Google nunca la ha rastreado.** La causa está aguas arriba: el hub `/noticias` figura como "Descubierta: actualmente sin indexar" y nunca fue rastreado, así que Google no llegó a los artículos enlazados desde él. Lo técnico está correcto (308 → 200, canonical y sitemap en orden): es presupuesto de rastreo por falta de autoridad. **Acción: solicitar indexación manual en GSC** de `/noticias`, la nota GACC y la de agosto |
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

### F · Traducciones

| # | Palanca | Estado | Detalle |
|---|---|---|---|
| F1 | **Paridad ES/EN en servicios** | ✅ Hecho (ago 2026) | Cobertura de 90–96%. Ver `TRADUCCIONES.md` |
| F2 | **Cuerpo de las noticias en inglés** | ⬜ No abordado | Beneficio de experiencia, no de posicionamiento. Se agranda con cada noticia nueva |
| F3 | **Páginas en inglés con URL propia** | ⬜ Evaluar sep-oct | Lo único que posiciona en inglés de verdad. Fuera del alcance de la mantención |

### E · Internacional — meses 4–5

| # | Palanca | Estado |
|---|---|---|
| E1 | **Baidu Webmaster + `/zh`** | Página creada, registro pendiente (requiere cuenta Baidu) |
| E2 | **Versión en inglés** | Justificada por las impresiones desde EE.UU. sin clics |

---

## Secuencia

**Agosto — atacar lo que ya muestra intención comercial**
1. ✅ Ampliar Asesorías en inocuidad (A1)
2. ✅ Ampliar Ciruelas deshidratadas (A1) — y de paso Maquinaria, Exportación y Representación
3. ✅ Limpieza técnica B1 + B2 (una tarde de trabajo)
4. ⬜ Iniciar altas de autoridad C1–C5 — **bloqueado: requiere datos y cuentas del cliente**
5. ✅ 2 noticias de agosto, ambas enlazando a su página de servicio (A2 + A3) — la segunda programada para el 18
6. ⬜ Desbloquear GA4 (D3) — **bloqueado: requiere habilitar las APIs en Google Cloud**

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

| Hito | Plazo | Estado (11 ago 2026) |
|---|---|---|
| Doblar los **clics a páginas interiores**: 11 → 22 en 28 días | Nov 2026 | ⬜ 12 hoy |
| 40–60 consultas reveladas | Sep 2026 | ⬜ 9 hoy (eran 7) |
| Keywords objetivo en rango 15–25 | Oct 2026 | ⬜ 29–80 hoy |
| Primera keyword comercial en página 1 | Nov 2026 | ⬜ ninguna |

> **Primera lectura de agosto (11 ago).** Las impresiones subieron de 113 a **148 (+31%)**,
> la posición media de 11,9 a **9,9** y las consultas reveladas de 7 a **9** — es el efecto
> esperado de las cinco páginas de servicio ampliadas la primera semana. Los clics todavía
> no se mueven (20 → 21), que es lo normal: primero aparecen las impresiones, los clics
> vienen cuando las posiciones entran a la primera página.

**Lo que no se promete:** una posición concreta en una fecha concreta. Llevar una consulta de
la posición 60 a la primera página toma de 3 a 6 meses con contenido y autoridad. Cualquier
promesa más precisa que eso es adivinanza.
