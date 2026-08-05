# Traducciones al inglés — cómo funciona y qué falta

**Actualizado:** 5 de agosto de 2026

---

## Cómo funciona hoy

El sitio traduce **del lado del cliente, con JavaScript**. Al pulsar "EN":

1. `translations.js` recorre todos los elementos con `data-i18n="clave"`.
2. Si la clave existe para el idioma destino, reemplaza el `innerHTML` del elemento.
3. Si la clave **no** existe, deja el contenido tal como está.

Ese último punto es importante: **una clave faltante no rompe nada, simplemente deja
el texto en español**. Por eso es posible tener páginas parcialmente traducidas sin
que se note un error.

### Dónde viven las traducciones

| Archivo | Qué contiene | Se carga en |
|---|---|---|
| `translations.js` | Navegación, pie, home | Todas las páginas |
| `page-translations.js` | Contenido original de servicios y fichas técnicas | Todas las páginas |
| `servicios-ampliado.i18n.js` | Contenido ampliado de agosto 2026 | **Solo `/servicios/`** |

El tercero está separado a propósito: pesa 74 KB y solo lo necesitan cinco páginas.
Meterlo en `page-translations.js` habría sumado ese peso a **todas** las visitas del
sitio, incluidas home y noticias.

---

## Estado actual de cobertura

| Página | Palabras | Traducibles | Cobertura |
|---|---|---|---|
| Asesorías en inocuidad | 1.771 | 1.647 | **93%** |
| Ciruelas deshidratadas | 1.457 | 1.313 | **90%** |
| Maquinaria agroindustrial | 1.363 | 1.305 | **96%** |
| Exportación agroindustrial | 1.213 | 1.130 | **93%** |
| Representación comercial | 1.016 | 950 | **94%** |
| **Noticias (todas)** | — | — | **0% del cuerpo** |

En las noticias se traducen la navegación, el pie y las migas de pan, pero **el titular
y el cuerpo del artículo permanecen en español**.

---

## ⚠️ Lo más importante de este documento

**La traducción por JavaScript no aporta nada al posicionamiento en inglés.**

Google indexa el HTML que el servidor entrega, y ese HTML está en español. El cambio de
idioma ocurre en el navegador, después de que el buscador ya leyó la página. En la
práctica:

- ✅ **Sirve** para que un visitante que llega y pulsa "EN" pueda leer el contenido.
- ❌ **No sirve** para aparecer en búsquedas en inglés.

El informe de julio de 2026 registró **15 impresiones desde Estados Unidos sin ningún
clic**. Ese interés no se convierte traduciendo por JavaScript.

### Qué haría falta para posicionar en inglés de verdad

Páginas con **URL propia** (`/en/servicios/...`), su HTML servido en inglés, y etiquetas
`hreflang` que le indiquen a Google la correspondencia entre ambas versiones. Es un
proyecto aparte del alcance de la mantención mensual, y conviene evaluarlo con datos:
si las impresiones desde mercados anglófonos crecen, se justifica; si no, no.

---

## Cómo agregar contenido sin romper la paridad

> **Regla:** todo contenido nuevo en una página de servicio va **dentro** del `<div>`
> que ya tiene `data-i18n`, y su traducción se agrega a `servicios-ampliado.i18n.js`.
> Si se agrega fuera, queda en español para siempre y nadie se entera.

Claves en uso:

| Página | Contenido ampliado | Preguntas frecuentes |
|---|---|---|
| Asesorías | `ase.ext` | `ase.faqx` |
| Ciruelas | `cir.ext` | `cir.faqx` |
| Maquinaria | `maq.ext` | `maq.faqx` |
| Exportación | `exp.ext` | `exp.faqx` |
| Representación | `rep.ext` | `rep.faqx` |

Cada clave guarda un **bloque completo de HTML**, no una frase suelta. Al editar hay
que actualizar las dos versiones, `es` y `en`.

### Verificar la paridad

```bash
node -e "global.window={translations:{es:{},en:{}}};require('./servicios-ampliado.i18n.js');
const t=window.translations;for(const k of Object.keys(t.es))if(!t.en[k])console.log('FALTA EN:',k);
console.log('claves:',Object.keys(t.es).length);"
```

Debe listar cero faltantes.

---

## Historial

- **Antes de agosto 2026:** las páginas de servicio estaban traducidas casi por completo.
- **Agosto 2026:** al ampliar las cinco páginas de servicio, el contenido nuevo se agregó
  sin marcas de traducción y la cobertura cayó a un rango de 21% a 35%. Se corrigió el
  mismo mes creando `servicios-ampliado.i18n.js`, y la cobertura subió a 90–96%.
- **Pendiente:** el cuerpo de las noticias sigue solo en español. No se abordó porque el
  beneficio es de experiencia y no de posicionamiento, y porque cada noticia nueva
  agrandaría el problema. Se resuelve de raíz con páginas en inglés con URL propia.
