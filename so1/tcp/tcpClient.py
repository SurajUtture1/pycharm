import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12345))
payload = 'hey server'

try:
    while True:
        client_socket.send(payload.encode('utf-8'))
        data = client_socket.recv(1024)
        print(str(data))
        more = input("send more input to the server")
        if more.lower() == 'y':
            payload = input("Enter the payload")
        else:
            break
except KeyboardInterrupt:
    print("Exited by user")
client_socket.close()
