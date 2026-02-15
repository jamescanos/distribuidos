import socket

# Create a TCP socket (IPv4)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server to all interfaces on port 5000
server.bind(("0.0.0.0", 5000))

# Listen for incoming connections
server.listen(1)

print("Servidor esperando conexión...")

# Accept a client connection
conn, addr = server.accept()
print(f"Cliente conectado desde {addr}")

# Receive the student's name from the client
student_name = conn.recv(1024).decode()

# Send a personalized message back to the client
response = f"Hola {student_name}, bienvenido a Programación Distribuida!"
conn.sendall(response.encode())

# Close the connection
conn.close()
server.close()