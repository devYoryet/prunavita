# Configuración del Visor de LinkedIn

Este documento explica cómo configurar el visor de publicaciones de LinkedIn en la página de Prunavita.

## Opción 1: Widget Oficial de LinkedIn (Recomendado)

### Pasos para configurar:

1. **Obtener el ID de tu empresa en LinkedIn:**
   - Ve a tu página de empresa en LinkedIn
   - La URL será algo como: `https://www.linkedin.com/company/tu-empresa/`
   - El ID numérico se encuentra en la configuración de la página o en la URL del embed

2. **Editar el archivo `index.html`:**
   - Busca la línea que dice: `<script type="IN/CompanyProfile" data-id="TU_COMPANY_ID"`
   - Reemplaza `TU_COMPANY_ID` con el ID numérico de tu empresa

3. **Ejemplo:**
   ```html
   <script type="IN/CompanyProfile" data-id="12345678" data-format="inline" data-related="false"></script>
   ```

## Opción 2: Iframe Directo (Alternativa)

Si el widget oficial no funciona, puedes usar un iframe directo:

1. **Obtener el código de embed de LinkedIn:**
   - Ve a tu página de empresa en LinkedIn
   - Haz clic en "Más" > "Insertar página"
   - Copia el código del iframe

2. **Editar el archivo `index.html`:**
   - Comenta el widget oficial (las líneas con `<script type="IN/CompanyProfile"`)
   - Descomenta el iframe (quita los `<!--` y `-->`)
   - Reemplaza la URL del iframe con el código que copiaste

## Personalización

### Cambiar el nombre de la empresa en el enlace de fallback:

1. Busca en `index.html` la línea:
   ```html
   <a href="https://www.linkedin.com/company/TU_COMPANY_NAME"
   ```

2. Reemplaza `TU_COMPANY_NAME` con el nombre de tu empresa en LinkedIn (sin espacios, en minúsculas)

### Ejemplo:
```html
<a href="https://www.linkedin.com/company/prunavita"
```

## Notas Importantes

- El widget de LinkedIn puede tardar unos segundos en cargar
- Asegúrate de que tu página de empresa en LinkedIn sea pública
- Si no ves las publicaciones, verifica que tu página tenga contenido publicado
- El visor es completamente responsive y se adapta a dispositivos móviles

## Solución de Problemas

### El widget no se muestra:
1. Verifica que el ID de la empresa sea correcto
2. Asegúrate de que tu página de LinkedIn sea pública
3. Prueba con el iframe alternativo

### El contenido no se actualiza:
- LinkedIn actualiza el contenido automáticamente cada cierto tiempo
- Puede tardar unos minutos en reflejar nuevas publicaciones

## Soporte

Si tienes problemas con la configuración, consulta la documentación oficial de LinkedIn:
https://www.linkedin.com/help/linkedin/answer/a521884
