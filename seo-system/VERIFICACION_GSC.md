# Verificación de prunavita.cl en Google Search Console

## Estado: ✅ RESUELTO (julio 2026)

La propiedad **`sc-domain:prunavita.cl`** está verificada y operativa. Se resolvió por la
**Opción A (propiedad de Dominio)**: el registro TXT sí quedó agregado en la zona DNS.

Comprobado el **3 de agosto de 2026** ejecutando `python scripts/google_connect.py`:

```
=== Google Search Console ===
  • sc-domain:prunavita.cl — permiso: siteFullUser
```

El sitio está **indexado y recibiendo tráfico orgánico**: 12 URLs con impresiones en los
últimos 28 días, home en posición media 1,7.

> **Para quien lea esto en el futuro:** este documento describía un problema de junio 2026
> que ya no existe. Si necesitas el estado actual de la medición, corre el script — es la
> única fuente confiable. La documentación envejece; los datos en vivo no.

---

## Cómo confirmarlo en 10 segundos

```bash
python scripts/google_connect.py
```

Si aparece `sc-domain:prunavita.cl — permiso: siteFullUser`, la verificación está vigente.
Si dijera "Sin propiedades verificadas", recién ahí aplica el historial de abajo.

---

## Historial — por qué falló en junio 2026

Se intentó verificar una propiedad de tipo **Dominio** ("Proveedor de nombres de dominio").
Ese método **solo acepta un registro TXT en el DNS** — ignora por completo el meta tag
del HTML. Google solo encontraba el TXT de SPF del correo, porque el TXT de verificación
nunca se había agregado al DNS.

**Token de verificación:** `google-site-verification=Q3Zx-Khqpz58KD23X6qKkk-OEHKFYfFjSgTwu-IJ3L4`
**DNS del dominio:** ns1/ns2/ns3.dnsmisitio.net (panel del hosting, zona DNS en cPanel)

> El meta tag que está en `index.html` sirve para el OTRO método (propiedad
> "Prefijo de URL" + "Etiqueta HTML"), no para la propiedad de Dominio.

### Cómo se resolvió (referencia si hay que rehacerlo)

1. Panel del hosting (cPanel) → **Zone Editor / Editor de zona DNS** → dominio `prunavita.cl`.
2. Agregar un registro:
   - **Tipo:** TXT
   - **Nombre/Host:** `@` (o `prunavita.cl.` o vacío, según el panel — significa el dominio raíz)
   - **Valor:** `google-site-verification=Q3Zx-Khqpz58KD23X6qKkk-OEHKFYfFjSgTwu-IJ3L4`
   - **TTL:** el que venga por defecto (3600)
3. Guardar. NO tocar el TXT existente de SPF (`v=spf1 ...`) — pueden convivir ambos.
4. Esperar propagación (minutos, hasta 24 h) y pulsar **Verificar** en Search Console.
5. Comprobar: <https://toolbox.googleapps.com/apps/dig/#TXT/prunavita.cl> debe mostrar
   el token junto al SPF.

## Acceso programático

La cuenta de servicio **`claude@android-1428a.iam.gserviceaccount.com`** está agregada como
usuario en la propiedad, lo que permite consultar GSC sin navegador desde
`scripts/google_connect.py`. La clave vive en `android-1428a-*.json` en la raíz — **está en
`.gitignore` y nunca debe subirse al repositorio**.
