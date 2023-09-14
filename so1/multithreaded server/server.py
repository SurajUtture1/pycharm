import socket
from _thread import *

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
d = 999
ThreadCount = 0

# Binding the socket server
try:
    server_socket.bind((host, d))
except socket.error as e:
    print(str(e))
print("waiting for connection")
server_socket.listen(5)


def client_thread(connection):
    connection.send(str.encode("welcome to the server"))
    while True:
        data = connection.recv(2048)
        reply = "Hello i am server" + data.decode("utf-8")
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()


while True:
    client, addr = server_socket.accept()
    print("connected to" + addr[0] + str(addr[1]))
    start_new_thread(client_thread, (client,))
    ThreadCount += 1
    print("ThreadNumber" + str(ThreadCount))
