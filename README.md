📲 BOT SMS con Twilio






✨ Descripción

Este script en Python permite enviar SMS de manera rápida y paralela usando Twilio.
Cada usuario ingresa sus propias credenciales de Twilio (Account SID, Auth Token y número de Twilio) y puede enviar mensajes a múltiples destinatarios simultáneamente mediante threads.

El bot muestra mensajes de estado en la consola para confirmar envíos y simular progreso.

⚙️ Características

Envío de SMS a múltiples destinatarios.

Ejecución paralela usando hilos (Thread) para mayor rapidez.

Los usuarios ingresan sus propias credenciales de Twilio.

Compatible con Python 3.10+ y macOS.

Simula mensajes de estado y confirmación de envío.

📦 Requisitos

Python 3.10 o superior

Librerías necesarias:

pip3 install twilio

🚀 Uso

Clona el repositorio:

git clone <tu-repositorio>
cd <tu-repositorio>


Ejecuta el script:

python3 bot.py


Ingresa tus credenciales de Twilio:

Account SID

Auth Token

Número de Twilio (ejemplo: +5215512345678)

Ingresa los números de teléfono y los mensajes a enviar:

+5215512345678|Hola, este es un mensaje de prueba
+5215598765432|Otro mensaje diferente


Los mensajes se enviarán en paralelo y se mostrará el SID de cada envío en la consola.

📝 Ejemplo de salida
=== BOT SMS ===
Ingresa tu Account SID de Twilio: ACXXXXXXXXXXXXXXXXXXXX
Ingresa tu Auth Token de Twilio: your_auth_token
Ingresa tu número de Twilio (ej. +5215512345678): +5215512345678

Número de teléfono (ej. +52155XXXXXXX, vacío para terminar): +5215512345678
Mensaje para +5215512345678: Hola mensaje

✅ Mensaje enviado a +5215512345678. SID: SMXXXXXXXXXXXXXXXXXXXX

⚠️ Advertencias

Cada usuario debe tener su propia cuenta y número de Twilio.

No es un bot de Telegram; funciona solo en consola.

Respeta las leyes locales sobre envío de SMS masivos.

🧑‍💻 Desarrollador

Alvaro Manzo
