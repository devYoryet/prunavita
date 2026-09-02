# Reporte Mensual SEO — Prunavita.cl

**Período:** Agosto 2026 (Mes 3 del plan · primer reporte con GSC **y** GA4)
**Elaborado por:** Yoryet Danoun · Pulsando Tech
**Para:** Felipe Catalán / equipo Prunavita
**Fecha de envío:** 31/08/2026
**Documento cliente:** `INF-PRU-SEO-2026-03` → `INFORME_MENSUAL_SEO_PRUNAVITA_AGOSTO2026.html`
**Fuentes:** Google Search Console (`sc-domain:prunavita.cl`) + Google Analytics 4 (`properties/541942768`)
**Ventana:** 1–28 ago vs 1–28 jul (28 días cada una; GSC consolida con 3 días de retraso)
**Reproducible con:** `python scripts/medicion_mensual.py --mes 2026-08`

---

## 1. Resumen ejecutivo

Mes **bueno en tracción, insuficiente en prueba comercial**. Las impresiones se multiplicaron por 15,
los clics se duplicaron y la posición media entró a la primera página (12,3 → 8,2). El hito que el plan
fijaba para **noviembre** —doblar los clics a páginas interiores— se cumplió en agosto con **32**.

Las dos advertencias que el informe al cliente no maquilla:

1. **El crecimiento tiene un solo motor.** 1.081 de las 1.531 impresiones vienen de la noticia del RSA.
   Es tráfico informativo: CTR 0,83%, 19 s de permanencia, 33% de interacción. El peor registro de
   retención del sitio.
2. **Las 5 keywords comerciales no se movieron** (29–76). Ya no es problema de contenido: falta
   autoridad externa, y eso depende de los accesos pedidos el 17 de agosto, aún sin respuesta.

**Hito nuevo del mes:** GA4 quedó operativo el 29 de agosto (`analyticsadmin.googleapis.com` estaba
`DISABLED` en el proyecto Cloud, no era permiso del cliente). Por primera vez hay cruce GSC × GA4.

---

## 2. Indicadores clave

| Indicador | Julio | Agosto | Variación |
|---|---:|---:|---|
| Impresiones | 105 | **1.531** | +1.358% |
| Clics | 21 | **43** | +105% |
| **Clics a páginas interiores** (métrica norte) | 10 | **32** | +220% |
| Posición media | 12,3 | **8,2** | mejora 4,1 |
| CTR | 20,00% | 2,81% | ver §5 |
| Páginas con impresiones | 12 | **16** | +4 |
| Consultas distintas reveladas | 6 | **30** | ×5 |
| Sesiones GA4 | 130 | **159** | +22% |
| Usuarios GA4 | 89 | **119** | +34% |
| Vistas de página | 227 | 242 | +7% |
| Eventos | 689 | 769 | +12% |

---

## 3. GA4 — canales y eventos

**Canales (sesiones / usuarios):** Organic Search 81/53 · Direct 59/54 · Organic Social 15/11 ·
**AI Assistant 4/4**.

**Eventos:** page_view 242 · session_start 159 · user_engagement 151 · first_visit 110 · scroll 55 ·
**ficha_view 31** · click 9 · file_download 6 · **ficha_download 4** · **contacto_iniciado 2**.

Las fichas técnicas se repusieron el 18 de agosto (15 PDF daban 404). En los 10 días siguientes son la
acción comercial más frecuente del sitio.

**Los 2 contactos iniciados** (los primeros medidos):

| Fecha | Página | Canal de origen |
|---|---|---|
| 18 ago | `/noticias/2026-08-maquinaria-agroindustrial-usada-que-revisar` | Organic Search |
| 19 ago | `/servicios/maquinaria-agroindustrial.html` | AI Assistant |

Los dos de **maquinaria**. Ninguno de ciruelas, cerezas ni de la noticia del RSA.

---

## 4. Cruce GSC × GA4 por página de entrada

| Página | Clics | Impr | CTR | Pos | Sesiones | Interac. | s/sesión |
|---|---:|---:|---:|---:|---:|---:|---:|
| `/` | 11 | 29 | 37,9% | 2,7 | 52 | 58% | 40 |
| Noticia RSA 2026 | 9 | **1.081** | 0,8% | 8,3 | 36 | 33% | 19 |
| Ciruelas deshidratadas | 5 | 134 | 3,7% | 7,0 | 4 | 50% | **66** |
| Cerezas chilenas | 4 | 59 | 6,8% | 6,4 | 11 | 45% | 7 |
| Maquinaria agroindustrial | 3 | 88 | 3,4% | 7,5 | 4 | 100% | 29 |
| Representación comercial | 3 | 36 | 8,3% | **3,9** | 3 | 33% | 6 |
| Noticia maquinaria usada | 2 | 8 | **25,0%** | **1,8** | 10 | 40% | **90** |
| Asesorías inocuidad | 2 | 60 | 3,3% | 11,8 | 3 | 67% | 86 |
| Fichas técnicas | 1 | 9 | 11,1% | 4,1 | 4 | 100% | 18 |
| Noticia jun — exportación ciruela | 1 | 2 | 50,0% | 8,0 | 5 | 100% | 65 |
| Noticia jul — GACC China | 1 | 19 | 5,3% | 5,0 | 4 | 50% | 15 |
| Exportación agroindustrial | 1 | 58 | 1,7% | 11,6 | 1 | 100% | 22 |

**Lecturas:**
- **Ciruelas** es la mejor página comercial: 66 s de permanencia. La gente la lee.
- **Cerezas** trae y pierde: 4 clics, 7 s. **No es falta de contenido**: con 2.241 palabras es la
  página más larga del sitio, con hero de producto y fichas enlazadas. Las consultas visibles que la
  encuentran son genéricas (`cerezas chile`, `cerezas`, `guindas chile`, `sweet aryana`): público que
  no es importador. Es desajuste de intención, no de profundidad. Ojo con la muestra: 11 sesiones.
- **Representación comercial** rankea 3,9 pero retiene 6 s: aparece para intención equivocada.
- **Noticia maquinaria usada** es el patrón a repetir: 8 impresiones, 25% CTR, 90 s, 1 contacto.

---

## 5. Por qué cayó el CTR de 20% a 2,81%

Aritmética, no deterioro. El denominador pasó de 105 a 1.531 impresiones, y las ~1.400 nuevas son de
consultas informativas del RSA. Los clics subieron igual (21 → 43).

**Efecto del cambio de título de la noticia RSA (G1, 17 ago):** 01–16 ago = 1 clic / 249 impr / CTR
0,40% / pos 8,0 → 18–25 ago = 4 clics / 588 impr / CTR 0,68% / pos 8,4. Mejora real pero marginal;
confirma que el problema es la intención de la consulta, no el título. **No insistir por esa vía.**

---

## 6. Keywords objetivo (ventana 90 días)

| Consulta | Posición | Impr | Clics | Estado |
|---|---:|---:|---:|---|
| compra maquinaria usada | 29,0 | 1 | 0 | en camino |
| asesoría en certificaciones | 43,0 | 1 | 0 | lejos |
| certificación brc chile | 49,3 | 11 | 0 | lejos |
| consultoría agroindustria | 55,0 | 1 | 0 | lejos |
| venta maquinaria manufactura | 75,7 | 6 | 0 | lejos |

Sin movimiento respecto de julio pese a la ampliación de las páginas de servicio. **Causa: autoridad.**

En página 1 hay dos consultas, ambas informativas: `rsa 2026` (pos 7,4) y
`reglamento sanitario de los alimentos 2026` (pos 9,0).

---

## 7. Estado de los hitos del plan

| Hito | Plazo | Hoy | Estado |
|---|---|---:|---|
| Doblar clics a interiores (11 → 22) | nov | **32** | ✅ Cumplido, 3 meses antes |
| 40–60 consultas reveladas | sep | 30 | 🟡 En camino (eran 6) |
| 5 keywords comerciales al rango 15–25 | oct | 29–76 | ❌ Frenado (falta autoridad) |
| Primera comercial en página 1 | nov | — | ❌ Pendiente |

---

## 8. Entregables de agosto

**Contratado (2 noticias/mes):** ✅ cumplido.
- 4 ago — *Actualización 2026 del Reglamento Sanitario de los Alimentos*
- 17 ago — *Maquinaria agroindustrial usada: qué revisar antes de comprar*

**Sin costo:**
- Página de **Cerezas chilenas** (única línea de producto sin página propia)
- **15 fichas técnicas repuestas** (daban 404 en producción; `.vercelignore` las excluía)
- **WhatsApp** como vía de contacto medida, en noticias y servicios
- 3 páginas de servicio ampliadas (Maquinaria 562 → 1.363 palabras) + paridad ES/EN
- Foto real por producto en cada ficha
- **GA4 destrabado** + `scripts/medicion_mensual.py` (un comando reproduce toda la medición)

34 commits en el mes.

---

## 9. Bloqueado por el cliente

Solicitud enviada el **17 de agosto**, sin respuesta a la fecha
(`seo-system/reportes/2026-08-solicitud-accesos.md`):

1. Google Business Profile (requiere código de verificación que solo recibe la empresa)
2. Registro en ProChile (RUT y credenciales)
3. Enlace del LinkedIn de empresa
4. Teléfono, dirección y correo comercial para las fichas de directorios
5. Membresías gremiales (Chilealimentos / Asoex) con perfil que enlace al sitio

Sin esto, los hitos de octubre y noviembre no son alcanzables por más contenido que se publique.

---

## 10. Plan de septiembre

1. **Duplicar la apuesta por maquinaria** — 1 de las 2 noticias, enlazada al servicio. Es el único tema
   con contactos probados.
2. **Reorientar Cerezas** — no ampliarla: reescribir title/H1/H2 hacia intención de importador
   (calibre, formato IQF/sulfitada, temporada, condiciones de embarque).
3. **Revisar Representación comercial** — alinear la página con la intención real de las consultas.
4. **Fichas técnicas al frente** — enlazarlas desde cada página de producto, no solo desde su sección.
5. **Directorios** — en cuanto lleguen los datos del §9. Textos redactados desde julio.

---

## 11. Cobro

| Concepto | Período | Valor | Estado |
|---|---|---:|---|
| Etapa 1 — implementación | jun 2026 | $570.000 | Pagado |
| Mantención mes 2 | jul 2026 | $150.000 | Pagado |
| **Mantención mes 3** | **ago 2026** | **$150.000** | **A cobrar** |

Sin saldos anteriores. Cobro al cierre de mes, según lo anunciado en el informe de julio.

---

## 12. Veredicto

> Mes bueno en tracción, insuficiente en prueba comercial, y con el freno puesto del lado del cliente.
> Si septiembre repite el volumen de agosto sin aumentar los contactos, el problema deja de ser SEO y
> pasa a ser de oferta.
