from twilio.rest import Client
from threading import Thread

def enviar_sms(client, twilio_number, numero, mensaje):
    try:
        message = client.messages.create(
            body=mensaje,
            from_=twilio_number,
            to=numero
        )
        print(f"✅ Mensaje enviado a {numero}. SID: {message.sid}")
    except Exception as e:
        print(f"❌ Error al enviar a {numero}: {e}")

def main():
    print("=== BOT SMS  ===")
    account_sid = input("Ingresa tu Account SID de Twilio: ").strip()
    auth_token = input("Ingresa tu Auth Token de Twilio: ").strip()
    twilio_number = input("Ingresa tu número de Twilio (ej. +5215512345678): ").strip()

    client = Client(account_sid, auth_token)

    destinatarios = []
    mensajes = []

    while True:
        numero = input("\nNúmero de teléfono (ej. +52155XXXXXXX, vacío para terminar): ").strip()
        if not numero:
            break
        mensaje = input(f"Mensaje para {numero}: ").strip()
        destinatarios.append(numero)
        mensajes.append(mensaje)

    if not destinatarios:
        print("⚠️ No se ingresaron destinatarios.")
        return

    # Crear y lanzar threads para envío paralelo
    threads = []
    for numero, mensaje in zip(destinatarios, mensajes):
        hilo = Thread(target=enviar_sms, args=(client, twilio_number, numero, mensaje))
        hilo.start()
        threads.append(hilo)

    # Esperar que todos los threads terminen
    for hilo in threads:
        hilo.join()

    print("\n✅ Todos los mensajes han sido enviados en paralelo.")

if __name__ == "__main__":
    main()
