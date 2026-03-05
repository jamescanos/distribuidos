import socket      # Librería para comunicación por red
import threading   # Librería para manejo de hilos
import time        # Librería para simular retraso

contador_clientes = 0  # Variable global compartida
lock = threading.Lock()  # Lock para evitar condiciones de carrera

# Función que atiende a cada cliente
def handle_client(conn, addr):
    global contador_clientes  # Permite modificar variable global

    # Muestra desde dónde se conecta el cliente
    print(f"Conexión recibida desde {addr}")

    # Recibe datos del cliente (máximo 1024 bytes)
    name = conn.recv(1024).decode()

    # Simula que la atención tarda 5 segundos
    print(f"Atendiendo a {name}...")
    time.sleep(5)

    # Sección crítica protegida con lock
    with lock:
        contador_clientes += 1
        numero = contador_clientes

    # Construye mensaje personalizado
    response = f"Hola {name}, eres el cliente número {numero}"

    # Envía respuesta al cliente
    conn.sendall(response.encode())

    print(f"Cliente {name} atendido correctamente.")

    # Cierra conexión
    conn.close()


# Crea el socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Asocia el socket al puerto 5000 en todas las interfaces
server.bind(("127.0.1.1", 5000))

# Pone el servidor en modo escucha
server.listen()

print("Servidor concurrente (threading) escuchando en puerto 5000...")

# Bucle infinito para aceptar clientes
while True:
    conn, addr = server.accept()

    # Crea un nuevo hilo para cada cliente
    thread = threading.Thread(
        target=handle_client,
        args=(conn, addr)
    )

    # Inicia el hilo
    thread.start()
