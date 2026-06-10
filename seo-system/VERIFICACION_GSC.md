# Verificación de prunavita.cl en Google Search Console

**Token:** `google-site-verification=Q3Zx-Khqpz58KD23X6qKkk-OEHKFYfFjSgTwu-IJ3L4`
**DNS del dominio:** ns1/ns2/ns3.dnsmisitio.net (panel del hosting, zona DNS en cPanel)

## Por qué falló la verificación (junio 2026)

Se intentó verificar una propiedad de tipo **Dominio** ("Proveedor de nombres de dominio").
Ese método **solo acepta un registro TXT en el DNS** — ignora por completo el meta tag
del HTML. Google solo encontró el TXT de SPF del correo, porque el TXT de verificación
nunca se agregó al DNS.

> El meta tag que está en `index.html` sirve para el OTRO método (propiedad
> "Prefijo de URL" + "Etiqueta HTML"), no para la propiedad de Dominio.

## Opción A — Propiedad de Dominio (recomendada)

Cubre www y sin www, http y https, y subdominios futuros (ej. una versión /zh/ o en.).

1. Entrar al panel del hosting (cPanel) → **Zone Editor / Editor de zona DNS** → dominio `prunavita.cl`.
2. Agregar un registro:
   - **Tipo:** TXT
   - **Nombre/Host:** `@` (o `prunavita.cl.` o vacío, según cómo lo pida el panel — significa el dominio raíz)
   - **Valor:** `google-site-verification=Q3Zx-Khqpz58KD23X6qKkk-OEHKFYfFjSgTwu-IJ3L4`
   - **TTL:** el que venga por defecto (3600)
3. Guardar. NO tocar el TXT existente de SPF (`v=spf1 ...`) — pueden convivir ambos.
4. Esperar la propagación (suele ser minutos, hasta 24 h) y pulsar **Verificar** de nuevo en Search Console.
5. Comprobar antes de reintentar: https://toolbox.googleapps.com/apps/dig/#TXT/prunavita.cl
   debe mostrar el token junto al SPF.

Si no hay acceso al cPanel, pedir al proveedor del hosting (dnsmisitio / soporte del plan)
que agregue ese TXT.

## Opción B — Propiedad "Prefijo de URL" (alternativa rápida)

1. En Search Console crear propiedad **Prefijo de URL** con `https://prunavita.cl/`.
2. Método de verificación: **Etiqueta HTML**.
3. El meta tag ya está en el `<head>` de `index.html` del repositorio:
   `<meta name="google-site-verification" content="Q3Zx-Khqpz58KD23X6qKkk-OEHKFYfFjSgTwu-IJ3L4">`
4. **Requisito:** que los cambios del repositorio estén desplegados en el hosting
   (merge del PR + subida de archivos). Sin deploy, Google no verá el tag.
5. OJO: si Search Console muestra un token DISTINTO para el método "Etiqueta HTML",
   hay que reemplazar el `content` del meta tag por ese token y volver a desplegar.

## Después de verificar (cualquiera de las dos opciones)

- [ ] Enviar `https://prunavita.cl/sitemap.xml` en GSC → Sitemaps.
- [ ] Solicitar indexación manual de las 7 URLs (Inspección de URLs → Solicitar indexación).
- [ ] Registrar la fecha de verificación en la memoria semanal.
