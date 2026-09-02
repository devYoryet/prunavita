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
| A3 | **Clusters de enlace interno** | ✅ Completo (12 ago 2026) | Cluster cerrado en los dos sentidos. Noticia → servicio: las 7 noticias enlazan desde el cuerpo a la página de su tema. Servicio → noticia: Asesorías 0→2, Exportación 0→2, Representación 1→3, Ciruelas 2→3, Maquinaria 1. Cada enlace va dentro del bloque `data-i18n`, con su par en inglés en `servicios-ampliado.i18n.js` |
| A4 | **FAQ con datos estructurados** | ✅ Ya estaba hecho | `FAQPage` presente en las cinco páginas de servicio. Figuraba como pendiente por error; se verificó el 17 ago leyendo el schema de cada página |
| A5 | **Página pilar de exportación** | Mes 4 | Guía extensa que concentre autoridad temática y reciba enlaces desde las noticias |
| A6 | **Página de cerezas** | ✅ Hecho (17 ago 2026) | El catálogo de fichas declara **7 productos de cereza** (IQF entera, descarozada IQF, pitted, sulfitada SO₂, fresca, deshidratada, pulpa) y no había ninguna página. Era la línea más grande del catálogo sin representación — ciruelas, con 4 fichas, sí la tenía. Espacio de consultas nuevo, sin solapamiento con ciruelas |
| A7 | **Frutillas y pulpas** | ⬜ Siguiente | Mismo hallazgo que A6, menor volumen: 2 fichas de frutilla IQF y 2 de pulpa, sin página. Evaluar una página conjunta después de medir cómo rinde la de cerezas |

### B · Técnico — rápido de ejecutar, efecto acotado

| # | Palanca | Estado | Detalle |
|---|---|---|---|
| B1 | **Borrar imágenes huérfanas** | ✅ Hecho | 17 MB en la raíz (`team-business.jpg` 13,2 MB, `global-export.jpg`, `quality-control.jpg`) que **ningún HTML referencia**. No afectan velocidad; sí ensucian el deploy |
| B2 | **Logo de datos estructurados** | ✅ Hecho (2.290→118 KB) | `logo_prunavita.png` pesa 2,3 MB y se declara como logo de la organización en el JSON-LD de 7 páginas. Debe bajar de 100 KB |
| B3 | **Imágenes a WebP** | Pendiente | Las portadas nuevas ya vienen a 1600×900; falta convertir el banco antiguo |
| B4 | **Schema `Service` y `BreadcrumbList`** | ✅ Hecho | Las cinco páginas de servicio **ya lo tenían** — figuraba pendiente por error. El hueco real estaba en las noticias: mostraban migas de pan en pantalla sin declararlas en schema. Corregido en las 7 el 17 ago |
| B5 | **Noticia GACC sin impresiones** | ✅ Resuelto (17 ago 2026) | **Se destrabó solo.** El hub `/noticias` ya se rastrea (6 impresiones) y **6 de las 7 noticias tienen impresiones**, la GACC incluida (4 impr, pos 5,2). No hizo falta la indexación manual: lo que abrió el paso fue la autoridad que sumaron las cinco páginas de servicio ampliadas. La lección es que el problema nunca fue técnico |
| B6 | **Indexación tras publicar** | Continuo | Enviar cada URL nueva a inspección en GSC el mismo día |

### G · Conversión — lo único que convierte visitas en clientes

> **Por qué se agrega esta sección.** El plan medía tráfico y no medía contactos. En agosto
> apareció el caso que lo dejó en evidencia: la noticia del Reglamento Sanitario acumuló
> **247 impresiones en posición 8,0 y trajo 1 clic**, y quien llegaba a leerla no tenía a
> mano ninguna forma directa de escribir. Traer gente y no darle salida es gastar el
> posicionamiento que costó tres meses conseguir.

| # | Palanca | Estado | Detalle |
|---|---|---|---|
| G1 | **Coincidencia título ↔ consulta** | ✅ Hecho (17 ago) | El título decía "Reglamento Sanitario 2026" y la consulta que la encuentra es "reglamento sanitario de los alimentos 2026" (113 impr), más 6 variantes de "rsa 2026". Título, meta, H1 y schema pasan a nombrar la norma completa **y** la sigla RSA, que juntas cubren las 7 consultas |
| G2 | **WhatsApp como vía de contacto** | ✅ Hecho (17 ago) | El sitio anunciaba "Teléfono / WhatsApp" y **no tenía un solo enlace `wa.me`**: la única salida era el formulario de la home, a dos clics de la noticia. Las 7 noticias, las 6 páginas de servicio y la home quedan con WhatsApp y **mensaje precargado propio de cada página**, así Prunavita sabe de qué contenido viene la consulta sin preguntarlo |
| G3 | **CTA en el tema de cada página** | ✅ Hecho (17 ago) | Dos noticias arrastraban el CTA genérico de plantilla. Ahora la del RSA ofrece adecuación normativa y la de maquinaria, evaluación de equipo usado |
| G4 | **Medir el contacto** | ✅ Instrumentado (17 ago) | Un clic a WhatsApp abre otra aplicación y saca al visitante del sitio: sin evento propio no quedaba registro. `trackContactClicks()` reporta a GA4 el evento `contacto_iniciado` con canal y página. **Ya se leen (D3 resuelto el 29 ago): 2 contactos entre el 18 y el 19 de agosto** — uno desde `/noticias/…maquinaria-usada` (canal AI Assistant) y otro desde `/servicios/maquinaria-agroindustrial.html` (Organic Search) |
| G5 | **Formulario de la home** | ⬜ Evaluar sep | Pide varios campos antes de dejar escribir. Medir con G4 cuánto convierte frente a WhatsApp antes de tocarlo |

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
| D3 | **Desbloquear GA4** | ✅ Resuelto (29 ago 2026) | El permiso en GA4 ya estaba dado por el cliente y la **Data API** ya estaba habilitada; lo único que faltaba era la **Analytics Admin API**, `DISABLED` en el proyecto `android-1428a` (601992161161). Se habilitó por Service Usage API con la propia cuenta de servicio. Propiedad: `prunavita` = **`properties/541942768`**, flujo `G-0G9GQYN4RE`. `scripts/google_connect.py` ya lee GA4. **Vínculo GA4 ↔ Search Console verificado el 29 ago**: la Admin API no lo expone (solo Google Ads y Search Ads 360), pero se comprueba pidiendo las métricas `organicGoogleSearch*` por `landingPagePlusQueryString` — responden y cuadran con GSC. Eso permite cruzar clic de búsqueda con interacción en la misma página |
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
5. ✅ 2 noticias de agosto, ambas enlazando a su página de servicio (A2 + A3) — la segunda publicada el 17
6. ✅ Desbloquear GA4 (D3) — resuelto el 29 ago: faltaba habilitar la Analytics Admin API en Google Cloud
7. ✅ Abrir la vía de contacto y hacerla medible (G1–G4)
8. ✅ Página de cerezas (A6), la línea de producto que no tenía ninguna

**Septiembre — convertir volumen en consultas** · detalle en `reportes/2026-09-plan.md`
> El plan de septiembre se reescribió el 2 de septiembre con los datos de cierre de agosto. Lo que
> figuraba aquí (ampliar Maquinaria y Exportación, FAQ con schema) **ya se hizo en agosto**: A1 quedó
> completo con las cinco páginas y A4 estaba hecho desde antes. El mes ya no es de profundizar
> contenido, es de convertir el tráfico que ya llega.

1. ⬜ **Enlazar las fichas técnicas desde las 5 páginas de servicio que no lo hacen** — mayor retorno
   por hora pendiente: 31 aperturas y 4 descargas en agosto, y solo `cerezas-chilenas` las enlaza
2. ⬜ **Reorientar Cerezas a intención de importador** (A6 bis) — no ampliarla: con 2.241 palabras es
   la página más larga del sitio. La encuentran consultas genéricas de consumidor
3. ⬜ **Noticia 1 (8 sep): maquinaria desde el lado del vendedor** — 3 de las 4 consultas visibles de
   esa página son de venta, no de compra, y `donde vender maquinaria usada` ya está en posición 6,0
4. ⬜ **Diagnosticar Representación comercial** — posición 3,9 y 6 s de permanencia: rankea para algo
   que la página no responde. Analizar antes de reescribir
5. ⬜ **Bing Webmaster Tools (D4)** — alimenta a ChatGPT/Copilot, y de ese canal salió 1 de los 2
   contactos de agosto
6. ⬜ **Noticia 2 (22 sep): temporada de cereza 2026/27** — ventana de compra de importadores
7. ⬜ WebP del banco antiguo (B3) · evaluar el formulario de la home contra WhatsApp (G5)
8. ⬜ Altas de autoridad C1–C6 — **sigue bloqueado. Corte el 15 de septiembre**

**Métrica nueva del mes:** clics a interiores **sin contar la noticia del RSA**. En agosto la métrica
norte dio 32, pero 9 son de esa noticia. Descontada quedan **23**. Sirve para saber si hay motor propio
o un solo golpe de suerte.

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

| Hito | Plazo | Estado (28 ago 2026) |
|---|---|---|
| Doblar los **clics a páginas interiores**: 11 → 22 en 28 días | Nov 2026 | ✅ **32** — cumplido tres meses antes. Sin la noticia del RSA serían 23 |
| 40–60 consultas reveladas | Sep 2026 | 🟡 **30** hoy (eran 7 en la línea base, 13 el 17 ago) |
| Keywords objetivo en rango 15–25 | Oct 2026 | ❌ 29–76 hoy. Sin movimiento pese a ampliar las cinco páginas: la causa es autoridad (C1–C6), y sigue bloqueada |
| Primera keyword comercial en página 1 | Nov 2026 | 🟡 `rsa 2026` en **posición 10,1** y `reglamento sanitario de los alimentos 2026` en **8,5** — informacionales, no comerciales, pero es la primera vez que el sitio toca página 1 con consultas de volumen real |

> **Segunda lectura de agosto (17 ago).** El salto es grande y tiene un motor identificable.
> Las impresiones pasaron de 148 a **445 (+201% en seis días, +294% desde la línea base)**, la
> posición media de 9,9 a **8,3**, las consultas reveladas de 9 a **13** y la métrica norte de
> 12 a **15**.
>
> El motor es **la noticia del Reglamento Sanitario**: sola acumula 247 impresiones en posición
> 8,0. Pegó en un tema que el sector está buscando ahora —`reglamento sanitario de los alimentos
> 2026` trae 113 impresiones y hay seis variantes más de "rsa 2026"—. Es la confirmación de que
> la palanca A2, noticias dirigidas a un término detectado en GSC, funciona.
>
> **El CTR bajó de 14,2% a 6,1% y eso no es un retroceso.** Las impresiones se triplicaron y los
> clics subieron de 21 a 27; el denominador creció más rápido que el numerador. El dato que
> importa es otro: las impresiones no-marca pasaron de 22 a **174**.
>
> **La lección incómoda:** esa noticia trajo 1 clic de sus 247 impresiones. El posicionamiento
> estaba, la coincidencia entre título y consulta no. Eso originó la sección G.

**Lo que no se promete:** una posición concreta en una fecha concreta. Llevar una consulta de
la posición 60 a la primera página toma de 3 a 6 meses con contenido y autoridad. Cualquier
promesa más precisa que eso es adivinanza.
