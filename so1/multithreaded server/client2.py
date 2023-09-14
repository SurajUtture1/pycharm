import socket

client_socket = socket.socket()
host = '127.0.0.1'
port = 999

print("waiting for connection")

try:
    client_socket.connect((host, port))
except socket.error as e:
    print(str(e))

Responce = client_socket.recv(1024)
print(Responce.decode("utf-8"))

while True:
    Input = input("say something")
    client_socket.send(str.encode(Input))
    response = client_socket.recv(1024)
    print(response.decode("utf-8"))
