import socket


client_socket = socket.socket()
client_socket.connect(('192.168.0.108', 9999))
name = input("Enter your name") #send name to the server
client_socket.send(bytes(name, 'utf-8'))
print(client_socket.recv(1024).decode())  # buffer size is 1024
