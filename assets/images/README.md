# Instrucciones para Agregar el Logo

Coloca el logo de Prunavita en este directorio con el nombre `logo.png`

El logo debe tener:
- Formato: PNG con fondo transparente (recomendado) o JPG
- Dimensiones recomendadas: 400x300px o similar (mantener proporción)
- Tamaño de archivo: Menor a 200KB para óptima performance

Una vez agregado el logo, actualiza las siguientes líneas en `index.html`:

## Navegación (línea ~24):
```html
<div class="logo">
    <img src="assets/images/logo.png" alt="Prunavita Logo" width="180" height="auto">
</div>
```

## Footer (línea ~550):
```html
<div class="footer-logo">
    <img src="assets/images/logo.png" alt="Prunavita" width="40" height="40">
    <span>Prunavita</span>
</div>
```

El logo que recibimos muestra:
- Dos ciruelas púrpuras oscuras (#4A2545 aprox)
- Una hoja verde (#5A7247 aprox)
- Texto "PrunaVita" en marrón oscuro
- Subtítulo "DRIED PRUNES"
- Fondo crema (#F5F1E8 aprox)

Estos colores ya están integrados en el diseño de la página.
