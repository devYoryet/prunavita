# Reporte Mensual SEO — Prunavita.cl

**Período:** Septiembre 2026 (Mes 4 del plan)
**Elaborado por:** Yoryet Danoun · Pulsando Tech
**Para:** Felipe Catalán / equipo Prunavita
**Fecha de envío:** 01/10/2026
**Documento cliente:** `INF-PRU-SEO-2026-04` → `INFORME_MENSUAL_SEO_PRUNAVITA_SEPTIEMBRE2026.html`
**Fuentes:** Google Search Console (`sc-domain:prunavita.cl`) + Google Analytics 4 (`properties/541942768`)
**Ventana:** 1–25 sep vs 1–25 ago (GSC consolida con 3 días de retraso; cifras a refrescar el 1 de octubre)
**Reproducible con:** `python scripts/medicion_mensual.py --mes 2026-09`

---

## 1. Resumen ejecutivo

**Septiembre no alcanzó ninguna de las tres metas que el propio plan se puso, y la causa es una sola:
el tráfico de agosto venía de un solo artículo y ese artículo se apagó.**

La noticia sobre el Reglamento Sanitario pasó de ~1.181 impresiones a **70**. Como representaba cerca
del 80% del volumen de agosto, al caer arrastró todo: las impresiones del sitio bajaron de 1.279 a
**590** y las sesiones de 139 a **84**.

Esto no es una sorpresa: el informe de agosto ya advirtió que ese pico era de público informativo, no
comercial, y el plan de septiembre creó un indicador específico —clics a interiores **sin contar el
RSA**— precisamente para detectar si había motor propio debajo. Lo detectó, y la respuesta fue que
todavía no lo hay.

**Lo que sí funcionó, y es el dato del mes:** la noticia del 2 de septiembre sobre venta de maquinaria
**creó superficie de búsqueda que no existía**. Siete consultas nuevas que en agosto no aparecían,
encabezadas por `vender maquinaria` con 37 impresiones. Están en posición 16 a 27 —página 2— así que
todavía no dan clics, pero es la primera vez que el sitio aparece por el lado vendedor del negocio,
que es de donde salieron los dos contactos de agosto.

**Y hay una señal de calidad:** el CTR subió de 2,81% a **4,92%**. Llega menos gente, pero la que
llega es más pertinente.

---

## 2. Indicadores clave

| Indicador | Ago 1–25 | Sep 1–25 | Variación |
|---|---:|---:|---|
| Clics | 36 | 29 | −19% |
| Impresiones | 1.279 | 590 | **−54%** |
| CTR | 2,81% | **4,92%** | **+75%** |
| Posición media | 8,3 | 8,9 | −0,6 |
| **Clics a páginas interiores** | 25 | **17** | −32% |
| Páginas con impresiones | 16 | **20** | +4 |
| Consultas distintas reveladas | 26 | 15 | −42% |
| Sesiones (GA4) | 139 | 84 | −40% |
| Usuarios (GA4) | 103 | 62 | −40% |
| `contacto_iniciado` | 2 | 2 | = |

Dos cifras suben y conviene no perderlas de vista: el **CTR** y las **páginas con impresiones** (de 16
a 20). El sitio aparece por más sitios distintos, aunque cada uno aporte poco.

---

## 3. Las tres metas del mes

El plan de septiembre fijó tres números por adelantado. Los tres se incumplieron.

| # | Indicador | Meta | Resultado | |
|---|---|---:|---:|---|
| 1 | `contacto_iniciado` | ≥ 4 | **2** | ❌ |
| 2 | Consultas distintas reveladas | 40–60 | **15** | ❌ |
| 3 | Clics a interiores sin contar el RSA | ≥ 30 | **17** | ❌ |

Los dos contactos del mes fueron el **7 de septiembre** (desde `/servicios/maquinaria-agroindustrial.html`,
tráfico orgánico) y el **10 de septiembre** (desde la portada). **Desde el 10 no ha entrado ninguno.**

Sobre la meta 2 conviene una precisión honesta: las "consultas reveladas" dependen de que Google
decida mostrarlas, y Google oculta las de bajo volumen. Al apagarse el RSA —que aportaba muchas
consultas de alto volumen sobre el reglamento— se fueron también sus consultas. No es que el sitio
aparezca por menos términos; es que menos términos superan el umbral que Google exige para mostrarlos.

---

## 4. Lo que sí construyó septiembre

Estas siete consultas **no existían en agosto**. Todas nacen de la noticia del 2 de septiembre:

| Consulta | Posición | Impresiones |
|---|---:|---:|
| `vender maquinaria` | 16,6 | **37** |
| `compra de maquina usada` | 26,9 | 11 |
| `vender maquinaria usada` | 22,0 | 1 |
| `regulación exportaciones agrícolas` | 41,0 | 1 |
| `ley 20606` | 3,0 | 1 |
| `dónde encuentro` | 5,0 | 1 |
| `prunita` (marca mal escrita) | 3,8 | 4 |

`vender maquinaria` es hoy la consulta con más impresiones de todo el sitio. Está en **posición 16,6**:
segunda página. Cero clics, porque a segunda página casi nadie llega. Pero el término ya está ganado
como territorio y subir de 16 a 8 es un trabajo mucho más corto que aparecer desde cero.

**Cerezas** también se movió: la página pasó de 109 a **143 impresiones** con 5 clics y posición 6,3.
La noticia del 24 de septiembre quedó **indexada en menos de una hora** y su primer día ya registró
9 impresiones en posición 4,6.

---

## 5. Entregables de septiembre

**Contratado (2 noticias investigadas/mes):** ✅ cumplido.

- **2 sep** — *Vender maquinaria agroindustrial usada en Chile: dónde, a qué precio y con qué papeles*
- **24 sep** — *Temporada de cereza chilena 2026/27: qué pasa con la fruta que no sale en fresco*

Ambas investigadas con fuentes citadas y enlazadas a su página de servicio.

**Sin costo adicional:**

| Qué | Resultado medible |
|---|---|
| Fichas técnicas enlazadas desde cada página de producto | Los 8 formatos de cereza y los 5 de ciruela abren su ficha en un clic |
| Diagnóstico de Representación comercial | Se descartó reescribirla con datos; se corrigió una pregunta duplicada en el contenido y en los datos estructurados |
| Conversión del banco de imágenes a WebP | **−2,1 MB (−40%)** de peso de imagen en todo el sitio |
| WhatsApp como acción principal en la portada | El formulario llevaba 3 inicios y **0 envíos** en 8 semanas |
| Alta y verificación en **Bing Webmaster Tools** | Verificado por dos métodos; Bing alimenta a ChatGPT y Copilot |
| Corrección del sitemap automático | Declaraba fechas viejas justo en las páginas recién modificadas |
| Banda de clientes en la portada | Prueba social sobre el hero |

---

## 6. Estado de los hitos del plan

| Hito | Plazo | Ago | Sep | Estado |
|---|---|---:|---:|---|
| Doblar clics a interiores (11 → 22) | nov | 32 | **17** | 🟡 Se cumplió en agosto y se perdió al apagarse el RSA |
| 40–60 consultas reveladas | sep | 30 | **15** | ❌ No alcanzado |
| 5 keywords comerciales al rango 15–25 | oct | 29–76 | **27–89** | ❌ **No alcanzable** — ver §7 |
| Primera comercial en página 1 | nov | — | — | ❌ Pendiente |

---

## 7. El bloqueo, con fecha de vencimiento cumplida

La solicitud de accesos se envió el **17 de agosto**. El plan de septiembre fijó el **15 de septiembre**
como punto de corte. **Al 28 de septiembre —42 días después— no hay respuesta.**

Las cinco keywords comerciales siguen donde estaban, y dos empeoraron:

| Consulta | Meta octubre | Agosto | Septiembre |
|---|---:|---:|---:|
| `compra maquinaria usada` | 15–25 | 29,0 | 29,0 |
| `certificación brc chile` | 15–25 | 47,5 | 36,8 |
| `asesoría en certificaciones` | 15–25 | 43,0 | 43,0 |
| `consultoría agroindustria` | 15–25 | 55,0 | 55,0 |
| `venta maquinaria manufactura` | 15–25 | 75,7 | 89,0 |

**Se declara formalmente no alcanzable el hito de octubre**, con la causa nombrada: no falta contenido
—las páginas se ampliaron en agosto y las posiciones no se movieron— falta **autoridad**, y la
autoridad depende de accesos que solo Prunavita puede entregar.

**El calendario ya no da, aunque la respuesta llegue esta semana.** Un enlace tarda entre dos y cuatro
meses en trasladarse a posiciones: uno conseguido a fines de septiembre rinde en **diciembre o enero**,
con el plan de seis meses terminado.

**Lo mínimo que destrabaría algo**, por orden de facilidad:

1. **Chileprunes y Chilealimentos (C3/C4)** — una sola pregunta de sí o no. Si son socios, aparecer en
   su directorio es el enlace más barato y más creíble del lote.
2. **LinkedIn de empresa (C6)** — cinco minutos, y multiplica el alcance de cada noticia.

Si de los seis solo se consiguen esos dos, el frente deja de estar completamente detenido.

---

## 8. Plan de octubre (mes 5)

1. **Empujar `vender maquinaria` de la página 2 a la página 1.** Es el activo nuevo del mes y el único
   territorio comercial donde ya aparecemos. Una noticia de refuerzo y enlazado interno hacia ella.
2. **Cerrar la ventana de cereza.** Octubre es el último mes en que los importadores cierran programa
   de temporada. La noticia del 24 ya rankea en posición 4,6: conviene capitalizarla, no abandonarla.
3. **Página pilar de exportación (A5)**, prevista para octubre en el plan de 6 meses.
4. **Directorios**, en cuanto lleguen los datos del §7. Los textos están redactados desde julio.

**Lo que no se hará y por qué:** el canal China/Baidu que el plan de seis meses situaba en meses 4–5
queda fuera. Sin autoridad en el mercado local y sin los accesos del §7, abrir un frente nuevo sería
repartir el mismo esfuerzo en más lugares.

---

## 9. Cobro

| Concepto | Período | Valor | Estado |
|---|---|---:|---|
| Etapa 1 — implementación | jun 2026 | $570.000 | Pagado |
| Mantención mes 2 | jul 2026 | $150.000 | Pagado |
| Mantención mes 3 | ago 2026 | $150.000 | **Por confirmar** |
| **Mantención mes 4** | **sep 2026** | **$150.000** | **A cobrar** |

Cobro al cierre de mes, según lo anunciado en el informe de julio.

> **Nota interna (no va al cliente):** el estado de la mantención de agosto quedó sin confirmar. Antes
> de emitir este informe hay que verificarlo; si está pagada, la línea se marca **Pagado** y el cobro
> del mes es de $150.000.

---

## 10. Veredicto

> **Este es el escenario que el plan de septiembre nombró por adelantado, y hay que decirlo sin rodeos.**
>
> Dos meses seguidos con dos contactos, y en septiembre con un CTR casi al doble —es decir, con tráfico
> más pertinente, no menos—. Cuando llega gente correcta y no escribe, el cuello de botella deja de
> estar en Google.
>
> El trabajo de posicionamiento tiene todavía margen claro: `vender maquinaria` en posición 16 es una
> oportunidad concreta y barata de capturar. Pero el salto de "aparecer" a "que le escriban" ya no
> depende solo de nosotros. Depende de **dos cosas que están del lado de Prunavita**: los accesos del
> §7, pendientes hace 42 días, y la oferta misma —qué se ofrece, a qué precio y con qué prueba— para
> el visitante que ya está leyendo la página correcta.
>
> Recomendación concreta para octubre: además del trabajo SEO, **media hora de conversación sobre la
> oferta comercial**. Con el tráfico actual, mover la tasa de contacto de 2 a 4 rinde más que duplicar
> las visitas.
