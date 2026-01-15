# Configuración de EmailJS para Formulario de Contacto

El formulario de contacto está configurado para enviar emails a **prunavita@prunavita.cl** usando EmailJS.

## ⚙️ Opción 1: Configurar EmailJS (Recomendado)

EmailJS permite enviar emails directamente desde el navegador sin necesidad de un servidor backend.

### Paso 1: Crear Cuenta en EmailJS

1. Ve a [https://www.emailjs.com/](https://www.emailjs.com/)
2. Crea una cuenta gratuita (hasta 200 emails/mes gratis)
3. Verifica tu email

### Paso 2: Agregar Servicio de Email

1. En el dashboard, ve a **Email Services**
2. Click en **Add New Service**
3. Selecciona tu proveedor (Gmail, Outlook, etc.)
4. Conecta tu cuenta **prunavita@prunavita.cl**
5. Copia el **Service ID** (ejemplo: `service_abc123`)

### Paso 3: Crear Template de Email

1. Ve a **Email Templates**
2. Click en **Create New Template**
3. Usa este template:

```
Subject: Nuevo contacto desde Prunavita - {{service}}

De: {{from_name}}
Email: {{from_email}}
Empresa: {{company}}
Teléfono: {{phone}}
Servicio de Interés: {{service}}

Mensaje:
{{message}}

---
Este mensaje fue enviado desde el formulario de contacto de www.prunavita.cl
```

4. Copia el **Template ID** (ejemplo: `template_xyz789`)

### Paso 4: Obtener Public Key

1. Ve a **Account** > **General**
2. Copia tu **Public Key** (ejemplo: `abcdef123456`)

### Paso 5: Actualizar index.html

Abre `index.html` y actualiza la línea 17:

```javascript
emailjs.init("TU_PUBLIC_KEY_AQUI");
```

### Paso 6: Actualizar script.js

Abre `script.js` y busca la línea ~78 (función handleSubmit), actualiza:

```javascript
emailjs.send('TU_SERVICE_ID', 'TU_TEMPLATE_ID', {
```

Ejemplo:
```javascript
emailjs.send('service_abc123', 'template_xyz789', {
```

### ✅ Probar el Formulario

1. Abre `index.html` en tu navegador
2. Llena el formulario de contacto
3. Envía el formulario
4. Deberías recibir un email en prunavita@prunavita.cl

---

## 📧 Opción 2: Usar Mailto (Alternativa Simple)

Si no quieres configurar EmailJS, el formulario automáticamente abrirá el cliente de correo del usuario.

**Ventajas:**
- No requiere configuración
- Funciona inmediatamente
- Sin límites de emails

**Desventajas:**
- El usuario debe tener configurado un cliente de correo
- Menos profesional
- No todos los usuarios tienen cliente de correo

---

## 🔧 Opción 3: Backend Propio (Avanzado)

Si prefieres usar tu propio servidor, puedes crear un endpoint en PHP, Node.js, Python, etc.

### Ejemplo con PHP:

Crea un archivo `contact.php`:

```php
<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = json_decode(file_get_contents('php://input'), true);

    $to = "prunavita@prunavita.cl";
    $subject = "Nuevo contacto - " . $data['service'];

    $message = "
    Nombre: {$data['name']}
    Email: {$data['email']}
    Empresa: {$data['company']}
    Teléfono: {$data['phone']}
    Servicio: {$data['service']}

    Mensaje:
    {$data['message']}
    ";

    $headers = "From: noreply@prunavita.cl\r\n";
    $headers .= "Reply-To: {$data['email']}\r\n";

    if (mail($to, $subject, $message, $headers)) {
        echo json_encode(['success' => true]);
    } else {
        echo json_encode(['success' => false, 'error' => 'Error al enviar']);
    }
}
?>
```

Luego actualiza `script.js` en la función `handleSubmit`:

```javascript
fetch('https://tudominio.com/contact.php', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
})
.then(response => response.json())
.then(result => {
    if (result.success) {
        this.showMessage('¡Gracias por contactarnos!', 'success');
        this.form.reset();
    } else {
        this.showMessage('Error al enviar', 'error');
    }
})
.catch(error => {
    this.showMessage('Error al enviar', 'error');
});
```

---

## 📱 Testing en Local

Para probar localmente con EmailJS:

1. Abre el archivo directamente en el navegador (file://)
2. O usa un servidor local:

```bash
# Con Python
python -m http.server 8000

# Con Node.js
npx serve

# Con PHP
php -S localhost:8000
```

Luego abre: `http://localhost:8000`

---

## ❓ Solución de Problemas

### El formulario no envía emails

1. Verifica que hayas actualizado las credenciales en index.html y script.js
2. Abre la consola del navegador (F12) para ver errores
3. Verifica que EmailJS esté cargado correctamente
4. Confirma que el template de EmailJS está activo

### Error: "EmailJS is not defined"

El CDN de EmailJS no se cargó. Verifica tu conexión a internet o descarga EmailJS localmente.

### El cliente de correo se abre en lugar de EmailJS

Esto significa que EmailJS no está configurado. El sistema usa mailto como fallback.

---

## 🎯 Recomendación

**Para Prunavita, recomiendo usar EmailJS** porque:

- Es gratis hasta 200 emails/mes (suficiente para una landing page)
- No requiere servidor backend
- Muy fácil de configurar (5 minutos)
- Profesional y confiable
- Emails llegan directamente a prunavita@prunavita.cl

---

## 📞 Soporte

Si necesitas ayuda con la configuración, contacta al desarrollador o consulta la documentación de EmailJS: https://www.emailjs.com/docs/
