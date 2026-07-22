# Conectar los datos de medición (Search Console + GA4)

**Meta:** poder ejecutar `python scripts/google_connect.py` y ver, en la terminal,
quién entró a Prunavita, desde dónde y con qué búsquedas. Es la base del reporte mensual.

> El script ya está listo y trae automáticamente: top consultas y páginas de Search Console
> y usuarios/sesiones/páginas/canales de GA4 (últimos 28 días). Solo falta la configuración
> de acceso de una vez.

---

## Orden correcto (importante)

La medición depende de 2 cosas que hoy faltan. Hacer en este orden:

### Paso 1 — Verificar la propiedad en Search Console (sin esto, GSC no tiene datos)
1. Entrar a https://search.google.com/search-console con la cuenta Google del proyecto.
2. **Agregar propiedad → "Prefijo de URL"** → `https://prunavita.cl/`
3. Método **"Etiqueta HTML"** → pulsar **Verificar**
   (el meta `google-site-verification=Q3Zx-...` ya está desplegado en el sitio).
4. Ir a **Sitemaps** → enviar `sitemap.xml`.
5. **Inspección de URLs** → pegar la home y las 5 páginas de servicio → **Solicitar indexación**.

> Sin este paso, `google_connect.py` mostrará "Sin propiedades verificadas". GA4 sí funciona igual.

### Paso 2 — Habilitar las APIs en Google Cloud
En https://console.cloud.google.com (proyecto `android-1428a`, el del `client_secret*.json`):
- **APIs y servicios → Biblioteca** → habilitar:
  - **Google Search Console API**
  - **Google Analytics Admin API**
  - **Google Analytics Data API**

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

## Estado actual (2026-07-21)

- [ ] Paso 1 — Propiedad verificada en GSC
- [ ] Paso 1 — Sitemap enviado + indexación solicitada
- [ ] Paso 2 — APIs habilitadas
- [ ] Paso 3 — URIs de redirección agregadas
- [ ] Paso 4 — `.google-token.json` generado y primer resumen obtenido
