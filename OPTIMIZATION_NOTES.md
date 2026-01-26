# Optimizaciones de Carga - Prunavita

## 🚀 Mejoras Implementadas

### 1. **Preload de Recursos Críticos**
- Se agregó `preload` para `styles.css`, `translations.js` y `script.js`
- Esto le dice al navegador que descargue estos archivos con prioridad

### 2. **CSS Crítico Inline**
- Se agregaron estilos críticos directamente en el `<head>` del HTML
- Esto previene el FOUC (Flash of Unstyled Content)
- Los estilos críticos incluyen:
  - Reset básico
  - Estilos del body y navbar
  - Loading screen

### 3. **Loading Screen**
- Pantalla de carga que se muestra mientras se cargan los recursos
- Se oculta automáticamente cuando todo está listo
- Spinner animado con los colores de la marca

### 4. **Optimización de Fuentes**
- Las fuentes de Google se cargan de forma asíncrona
- Se usa `media="print"` y luego se cambia a `all` cuando carga
- Fallback con `<noscript>` para navegadores sin JavaScript

### 5. **Scripts con Defer**
- Los scripts se cargan con `defer` para no bloquear el renderizado
- Se ejecutan después de que el HTML esté completamente parseado

### 6. **DNS Prefetch**
- Se agregó `dns-prefetch` para Google Fonts
- Acelera la resolución de DNS

## 📋 Recomendaciones Adicionales para cPanel

### 1. **Habilitar Compresión GZIP**
En cPanel, ve a:
- **Optimize Website** o **Compresión**
- Habilita GZIP para HTML, CSS y JS

### 2. **Habilitar Caché del Navegador**
Agrega un archivo `.htaccess` en la raíz con:
```apache
# Cache para CSS y JS
<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType text/css "access plus 1 year"
    ExpiresByType application/javascript "access plus 1 year"
    ExpiresByType image/jpeg "access plus 1 year"
    ExpiresByType image/png "access plus 1 year"
</IfModule>
```

### 3. **Minificar Archivos (Opcional)**
Puedes minificar `styles.css` y `script.js` para reducir el tamaño:
- Usa herramientas como: https://www.minifier.org/
- O plugins de cPanel si están disponibles

### 4. **CDN para Fuentes (Opcional)**
Si las fuentes cargan lento, considera:
- Descargar las fuentes y servirlas desde tu hosting
- O usar un CDN más rápido

## 🔍 Verificar que Funciona

1. **Abre las DevTools** (F12)
2. Ve a la pestaña **Network**
3. Recarga la página
4. Verifica que:
   - `styles.css` tiene prioridad "High"
   - Los scripts se cargan con `defer`
   - El loading screen desaparece cuando todo carga

## ⚠️ Notas Importantes

- El loading screen tiene un timeout de 2 segundos como fallback
- Si el CSS no carga, el contenido seguirá siendo visible (sin estilos)
- Los estilos críticos aseguran que al menos lo básico se vea inmediatamente

## 🐛 Solución de Problemas

### Si el loading screen no desaparece:
- Verifica que los archivos JS se carguen correctamente
- Revisa la consola del navegador por errores
- Asegúrate de que los archivos estén en la ubicación correcta

### Si aún hay FOUC:
- Verifica que el CSS crítico inline esté presente
- Asegúrate de que `styles.css` se cargue correctamente
- Revisa la velocidad de conexión del servidor
