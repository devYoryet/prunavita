# Conectar los datos de medición (Search Console + GA4)

**Meta:** poder ejecutar `python scripts/google_connect.py` y ver, en la terminal,
quién entró a Prunavita, desde dónde y con qué búsquedas. Es la base del reporte mensual.

## Estado en una línea (3 de agosto de 2026)

**Search Console: ✅ operativo.** **GA4: ⏳ falta acceso.** Corre el script y lo ves.

---

## Cómo se autentica hoy

Se resolvió con **cuenta de servicio**, no con el flujo OAuth de navegador. Es mejor para
reportes: no expira, no pide login y funciona desatendido.

- Clave: `android-1428a-*.json` en la raíz (**en `.gitignore`**, nunca al repositorio).
- Identidad: `claude@android-1428a.iam.gserviceaccount.com`
- Ya está agregada como usuario en la propiedad de GSC → por eso funciona.

Los pasos 3 y 4 de más abajo (URIs de redirección, `.google-token.json`) son del método OAuth
antiguo. **Se conservan solo como respaldo**; hoy no hacen falta.

---

## Paso 1 — Search Console ✅ HECHO

Propiedad **`sc-domain:prunavita.cl`** verificada, con permiso `siteFullUser`.
Se hizo por propiedad de **Dominio** (registro TXT en la zona DNS), no por etiqueta HTML.
Detalle e historial en `VERIFICACION_GSC.md`.

El sitio está indexado y con tráfico orgánico: 12 URLs con impresiones en los últimos 28 días.

## Paso 2 — APIs en Google Cloud ⏳ PARCIAL

En https://console.cloud.google.com (proyecto `android-1428a`) →
**APIs y servicios → Biblioteca**:

- ✅ **Google Search Console API** — habilitada (por eso GSC responde).
- ⏳ **Google Analytics Admin API** — falta.
- ⏳ **Google Analytics Data API** — falta.

## Paso 2b — Dar acceso a GA4 ⏳ PENDIENTE (único bloqueo real hoy)

En GA4 (propiedad `G-0G9GQYN4RE`) → **Administrar → Gestión de accesos a la propiedad** →
agregar `claude@android-1428a.iam.gserviceaccount.com` con rol **Lector**.

Sin esto el script imprime:

```
=== Google Analytics (GA4) ===
  No se pudo leer GA4. Falta un paso de configuración:
```

GA4 recopila datos desde junio 2026 — están ahí, solo no se pueden leer desde el script.
Es lo que falta para sumar comportamiento (rebote, páginas por sesión, conversiones) a los
datos de búsqueda que ya entrega Search Console.

---

## Método OAuth antiguo (respaldo — hoy no hace falta)

### Paso 3 — Registrar la URI de redirección OAuth
Por esto falló la conexión en junio: el cliente OAuth no tiene URIs de redirección.
- **APIs y servicios → Credenciales** → abrir el cliente OAuth "Web" (`601992161161-...`).
- En **URIs de redirección autorizados**, agregar exactamente:
  - `http://localhost:8091/`
  - `http://localhost:8090/`  (respaldo)
- Guardar. (También agregar tu correo como usuario de prueba en la **pantalla de consentimiento**
  si la app está en modo "Testing".)

### Paso 4 — Ejecutar la conexión (una sola vez)
```bash
pip install google-api-python-client google-auth-oauthlib google-auth   # si falta
python scripts/google_connect.py
```
- El script imprime una URL. Ábrela en el navegador, inicia sesión con la cuenta del proyecto
  y **acepta los permisos** (solo lectura de Search Console y Analytics).
- Al terminar, se guarda `.google-token.json` (ignorado por git) y **ya no hay que reautorizar**.
- Vuelve a correr `python scripts/google_connect.py` cuando quieras el resumen actualizado.

---

## Qué vas a ver (ejemplo de salida)

```
=== Google Search Console ===
  • https://prunavita.cl/ — permiso: siteOwner
  Rendimiento de https://prunavita.cl/ — 2026-06-23 a 2026-07-21:
  — Top consultas (keywords) —
    prunavita                          clics=5 impr=40 pos=1.2
    ...
=== Google Analytics (GA4) ===
  Cuenta: Prunavita
    • Prunavita - GA4 (ID: 123456789) — PROPERTY_TYPE_ORDINARY
        ¿Alguien entró? últimos 28 días → usuarios=37, sesiones=52
        Top páginas: / , /servicios/ciruelas-deshidratadas.html ...
        Canales: Direct, Organic Search, Referral, Organic Social ...
```

- **"usuarios / sesiones"** = cuánta gente intentó conectar / entró al sitio.
- **"Canales"** = de dónde llegan (Directo, Google orgánico, LinkedIn, un directorio, etc.).
- **"Top consultas"** = con qué palabras encontraron a Prunavita en Google.

---

## Seguridad

- `.google-token.json` y `client_secret*.json` están en `.gitignore` — **nunca** se suben al repo.
- Los permisos son **solo lectura** (`webmasters.readonly`, `analytics.readonly`).
- Si alguna vez se filtra el token, revocar en https://myaccount.google.com/permissions.

## Estado actual (2026-08-03, verificado ejecutando el script)

- [x] **Paso 1 — Propiedad verificada en GSC** (`sc-domain:prunavita.cl`, `siteFullUser`)
- [x] **Sitio indexado** — 12 URLs con impresiones, home en posición media 1,7
- [x] **Search Console API habilitada** y consultable sin navegador
- [x] **Cuenta de servicio con acceso a GSC** (`claude@android-1428a.iam.gserviceaccount.com`)
- [ ] **Analytics Admin API + Analytics Data API habilitadas** ← falta
- [ ] **Cuenta de servicio como Lector en GA4** ← falta (bloqueo único)

> Este bloque se desactualiza rápido. **La fuente de verdad es el script**, no esta lista:
> `python scripts/google_connect.py`. Actualiza este bloque cada vez que cambie algo,
> y ponle la fecha en que lo verificaste.
