import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.1.1", 5000))

name = input("Ingresa tu nombre: ")
client.sendall(name.encode())

response = client.recv(1024).decode()
print(response)

client.close()
