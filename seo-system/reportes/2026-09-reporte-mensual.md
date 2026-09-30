# Reporte Mensual SEO — Prunavita.cl

**Período:** Septiembre 2026 (Mes 4 del plan)
**Elaborado por:** Yoryet Danoun · Pulsando Tech
**Para:** Felipe Catalán / equipo Prunavita
**Fecha del documento:** 30/09/2026 · **envío:** 01/10/2026
**Documento cliente:** `INF-PRU-SEO-2026-04` → `INFORME_MENSUAL_SEO_PRUNAVITA_SEPTIEMBRE2026.html`
y su PDF `Informe Mensual SEO — Septiembre 2026 _ Prunavita.pdf` (11 páginas A4)
**Fuentes:** Google Search Console (`sc-domain:prunavita.cl`) + Google Analytics 4 (`properties/541942768`)
**Ventana:** 1–27 sep vs 1–27 ago (GSC consolida con 3 días de retraso)
**Reproducible con:** `python scripts/medicion_mensual.py --mes 2026-09`

---

## 1. Resumen ejecutivo

Mes de dos caras. **Los tres objetivos numéricos no se alcanzaron**, por una causa única y anticipada.
**Y se destrabaron dos frentes que llevaban meses detenidos.**

**La caída:** la noticia del RSA pasó de ~1.181 impresiones a **70**. Como era cerca del 80% del
volumen de agosto, al caer arrastró todo: las impresiones bajaron de 1.463 a **618** y las sesiones
de 155 a **86**.

No fue sorpresa. El informe de agosto advirtió que ese pico era público informativo, y el plan de
septiembre creó un indicador específico —clics a interiores **sin contar el RSA**— para detectar si
había motor propio debajo. Lo detectó: todavía no lo hay.

**Los dos avances del mes:**

1. **Google Business Profile creado.** Era la gestión C1, detenida desde el 17 de agosto.
2. **Bing Webmaster Tools verificado.** Token publicado por dos métodos y comprobado en vivo.

**Territorio nuevo:** la noticia del 2 de septiembre creó **siete consultas que no existían en
agosto**, encabezadas por `vender maquinaria` (37 impresiones), hoy la consulta con más impresiones
de todo el sitio. Están en posición 16 a 27 —página 2— así que aún no dan clics.

**Señal de calidad:** el CTR subió de 2,80% a **5,02%**. Llega menos gente y más pertinente.

---

## 2. Indicadores clave

| Indicador | Ago 1–27 | Sep 1–27 | Variación |
|---|---:|---:|---|
| Clics | 41 | 31 | −24% |
| Impresiones | 1.463 | 618 | **−58%** |
| CTR | 2,80% | **5,02%** | **+79%** |
| Posición media | 8,2 | 8,9 | −0,7 |
| **Clics a páginas interiores** | 30 | **18** | −40% |
| Páginas con impresiones | 16 | **20** | +4 |
| Consultas distintas reveladas | 29 | 16 | −45% |
| Sesiones (GA4) | 155 | 86 | −45% |
| Usuarios (GA4) | 117 | 64 | −45% |
| `contacto_iniciado` | 2 | 2 | = |

Suben dos: **CTR** y **páginas con impresiones** (16 → 20). Diversificación, que es lo contrario del
problema de concentración de agosto.

---

## 3. Las tres metas del mes

| # | Indicador | Meta | Resultado | |
|---|---|---:|---:|---|
| 1 | `contacto_iniciado` | ≥ 4 | **2** | ❌ |
| 2 | Consultas distintas reveladas | 40–60 | **16** | ❌ |
| 3 | Clics a interiores sin contar el RSA | ≥ 30 | **18** | ❌ |

Los dos contactos: **7 sep** (`/servicios/maquinaria-agroindustrial.html`, orgánico) y **10 sep**
(portada). **Desde el 10 no ha entrado ninguno.**

Precisión sobre la meta 2: las consultas reveladas dependen de que Google decida mostrarlas y oculta
las de bajo volumen. Al apagarse el RSA se fueron sus consultas, que eran muchas y de alto volumen.
No es que el sitio aparezca por menos términos: es que menos términos superan el umbral.

---

## 4. Lo que sí construyó septiembre

Siete consultas que **no existían en agosto**, todas nacidas de la noticia del 2 de septiembre:

| Consulta | Posición | Impresiones |
|---|---:|---:|
| `vender maquinaria` | 16,6 | **37** |
| `compra de maquina usada` | 26,9 | 11 |
| `vender maquinaria usada` | 22,0 | 1 |
| `regulación exportaciones agrícolas` | 41,0 | 1 |
| `ley 20606` | 3,0 | 1 |
| `dónde encuentro` | 5,0 | 1 |
| `prunita` (marca mal escrita) | 3,8 | 4 |

Subir de 16 a 8 es mucho más corto que aparecer desde cero. Es el objetivo número uno de octubre.

**Cerezas:** la página pasó de 109 a **143 impresiones**, 5 clics, posición 6,3. La noticia del 24
quedó **indexada en menos de una hora** y su primer día registró 9 impresiones en posición 4,6.

---

## 5. Entregables de septiembre

**Contratado (2 noticias investigadas/mes):** ✅ cumplido.

- **2 sep** — *Vender maquinaria agroindustrial usada en Chile: dónde, a qué precio y con qué papeles*
- **24 sep** — *Temporada de cereza chilena 2026/27: qué pasa con la fruta que no sale en fresco*

**Presencia en buscadores:**

| Gestión | Estado | Para qué sirve |
|---|---|---|
| Google Business Profile | ✅ Creado | Marca en Google y Maps, con panel propio |
| Bing Webmaster Tools | ✅ Verificado | Bing alimenta ChatGPT y Copilot |

**Sin costo adicional:**

| Qué | Resultado medible |
|---|---|
| Fichas técnicas enlazadas desde cada página de producto | 8 formatos de cereza y 5 de ciruela a un clic |
| Diagnóstico de Representación comercial | Se descartó reescribirla con datos; se corrigió una pregunta duplicada |
| Conversión del banco de imágenes a WebP | **−2,1 MB (−40%)** de peso de imagen |
| WhatsApp como acción principal en la portada | El formulario llevaba 3 inicios y **0 envíos** en 8 semanas |
| Corrección del sitemap automático | Declaraba fechas viejas en las páginas recién modificadas |
| `.vercelignore` por patrón | Los informes de cobro estaban listados uno por uno: olvidar uno los publicaba |

---

## 6. Estado de los hitos del plan

| Hito | Plazo | Ago | Sep | Estado |
|---|---|---:|---:|---|
| Doblar clics a interiores (11 → 22) | nov | 32 | **18** | 🟡 Cumplido en agosto, perdido al apagarse el RSA |
| 40–60 consultas reveladas | sep | 30 | **16** | ❌ No alcanzado |
| 5 keywords comerciales al rango 15–25 | oct | 29–76 | **27–89** | ❌ **No alcanzable** — ver §7 |
| Primera comercial en página 1 | nov | — | — | ❌ Pendiente |

> **Ojo con las dos cifras de "consultas reveladas".** En §2 agosto son **29** (ventana 1–27, para
> comparar contra el mismo tramo de septiembre) y aquí **30** (mes completo, que es como se comprometió
> el hito). Ambas correctas, ventanas distintas. El informe de cliente lo aclara al pie de la tabla.

---

## 7. Las gestiones del cliente: 2 de 6 resueltas

Solicitud del **17 de agosto**. Este mes hubo el primer movimiento desde entonces.

| # | Gestión | Estado | Qué destraba |
|---|---|---|---|
| C1 | Google Business Profile | ✅ **Resuelta** | Presencia de marca en Google y Maps |
| D4 | Bing Webmaster Tools | ✅ **Resuelta** | Canal hacia ChatGPT y Copilot |
| C2 | ProChile — directorio de exportadores | ⬜ Pendiente | El enlace de mayor confianza disponible |
| C3/C4 | Chileprunes / Chilealimentos | ⬜ Pendiente | Enlace de gremio, el más fácil de obtener |
| C6 | LinkedIn de empresa | ⬜ Pendiente | Difusión de cada noticia + enlace estable |
| C5 | Alibaba / Made-in-China | ⬜ Pendiente | Enlace + canal asiático |

**Por qué esto no salva todavía el hito de octubre.** GBP y Bing construyen *presencia de marca*:
ayudan a que encuentren a Prunavita cuando la buscan por su nombre. Las cinco keywords comerciales
dependen de otra cosa —**enlaces desde sitios del rubro**— que es lo que aportarían ProChile, los
gremios y LinkedIn. Son justamente las que siguen pendientes.

| Consulta | Meta octubre | Agosto | Septiembre |
|---|---:|---:|---:|
| `compra maquinaria usada` | 15–25 | 29,0 | 29,0 |
| `certificación brc chile` | 15–25 | 47,5 | 36,8 |
| `asesoría en certificaciones` | 15–25 | 43,0 | 43,0 |
| `consultoría agroindustria` | 15–25 | 55,0 | 55,0 |
| `venta maquinaria manufactura` | 15–25 | 75,7 | 89,0 |

**Se mantiene la declaración de no alcanzable** para el hito de octubre: un enlace tarda 2–4 meses en
trasladarse a posiciones, así que las cuatro gestiones pendientes, aunque se resolvieran esta semana,
rendirían en diciembre o enero.

---

## 8. Plan de octubre (mes 5)

1. **Empujar `vender maquinaria` de la página 2 a la página 1.** Activo nuevo y único territorio
   comercial donde ya aparecemos. Noticia de refuerzo + enlazado interno dirigido.
2. **Cerrar la ventana de cereza.** Octubre es el último mes de programa de temporada. La noticia del
   24 ya rankea en 4,6.
3. **Completar el Google Business Profile.** Creada la ficha, lo que rinde es llenarla: categoría,
   descripción, productos, horario, fotos reales y primeras reseñas. Una ficha vacía no convierte.
4. **Página pilar de exportación (A5)**, prevista para octubre en el plan de 6 meses.
5. **Directorios**, en cuanto lleguen los datos del §7. Textos redactados desde julio.

**Fuera de alcance:** China/Baidu. Sin autoridad local y con cuatro gestiones detenidas, abrir un
frente nuevo es repartir el mismo esfuerzo en más lugares.

---

## 9. Cobro

| Concepto | Período | Valor | Estado |
|---|---|---:|---|
| Etapa 1 — implementación | jun 2026 | $570.000 | Pagado |
| Mantención mes 2 | jul 2026 | $150.000 | Pagado |
| Mantención mes 3 | ago 2026 | $150.000 | **Por confirmar** |
| **Mantención mes 4** | **sep 2026** | **$150.000** | **A cobrar** |

> **Nota interna (no va al cliente):** el estado de la mantención de agosto sigue sin confirmar. Si
> está pagada, la línea se marca **Pagado** y el cobro del mes es de $150.000; si no, son $300.000.
> Verificar antes de enviar. Ver [[prunavita-contrato-y-cobros]].

---

## 10. Veredicto

> Dos meses seguidos con dos contactos, y en septiembre con un CTR casi al doble —tráfico *más*
> pertinente, no menos—. Cuando llega gente correcta y no escribe, el cuello de botella deja de estar
> en Google.
>
> El posicionamiento tiene margen claro: `vender maquinaria` en posición 16 es una oportunidad barata
> de capturar. Y con GBP y Bing resueltos, el frente de presencia dejó de estar detenido.
>
> Pero el salto de *aparecer* a *que le escriban* depende de dos cosas del lado de Prunavita: las
> cuatro gestiones pendientes y **la oferta comercial** —qué se ofrece, a qué precio, con qué prueba—
> para el visitante que ya está en la página correcta.
>
> Recomendación para octubre: además del SEO, **media hora de conversación sobre la oferta**. Con el
> tráfico actual, mover la tasa de contacto de 2 a 4 rinde más que duplicar las visitas.
