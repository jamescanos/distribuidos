import asyncio  # Importa la librería para programación asíncrona

# Función que maneja cada cliente (coroutine)
async def handle_client(reader, writer):
    # Espera datos del cliente (máximo 1024 bytes)
    data = await reader.read(1024)

    # Convierte los bytes recibidos en texto
    name = data.decode()

    # Construye el mensaje de respuesta
    response = f"Hola {name}"

    # Envía la respuesta al cliente (en bytes)
    writer.write(response.encode())

    # Espera a que los datos se envíen completamente
    await writer.drain()

    # Cierra la conexión con el cliente
    writer.close()


# Función principal del servidor
async def main():
    # Crea el servidor en la IP 0.0.0.0 y puerto 5000
    # handle_client será ejecutado por cada nueva conexión
    server = await asyncio.start_server(
        handle_client, "0.0.0.0", 5000
    )

    # Mantiene el servidor activo
    async with server:
        # El servidor queda escuchando indefinidamente
        await server.serve_forever()


# Ejecuta el event loop principal
asyncio.run(main())
