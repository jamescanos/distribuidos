import socket  # Librería de red
import time    # Para medir tiempo

# Crea el socket TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta al servidor local en puerto 5000
client.connect(("127.0.1.1", 5000))

# Solicita nombre al usuario
name = input("Ingresa tu nombre: ")

# Guarda tiempo inicial
start_time = time.time()

# Envía nombre al servidor
client.sendall(name.encode())

# Espera respuesta
response = client.recv(1024).decode()

# Guarda tiempo final
end_time = time.time()

# Muestra mensaje recibido
print(response)

# Muestra tiempo total
print(f"Tiempo de atención: {round(end_time - start_time, 2)} segundos")

# Cierra conexión
client.close()
