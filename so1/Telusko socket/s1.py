import socket

server_socket = socket.socket()
print("socket created")

server_socket.bind(('192.168.0.108', 9999))  # range of port number is 0 to 65535
server_socket.listen(3)
print("waiting for connection")

while True:
    client_socket, addr = server_socket.accept()
    print("connected with ", addr, name)
    name = client_socket.recv(1024).decode()#receive from client
    client_socket.send(bytes("welcome to telusko", 'utf-8'))
    client_socket.close()
