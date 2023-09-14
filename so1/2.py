import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket object
# server bind the socket to specific ip and port and it listen the request came from ip and port
server_socket.bind(('192.168.0.108', 123))  # binding
server_socket.listen(5)

while True:
    print("server waiting for connection: ")
    client_socket, addr = server_socket.accept()  # initiates the connection with client and holding the address of client
    print("client connected from", addr)
    while True:                                  # get the data and send the data to the client
        data = client_socket.recv(1024)                 # receive the data
        if not data or data.decode('utf-8') == 'END':              #if data is not receive or missing
            break
        print("received from the client : ", data.decode("utf-8"))
        try:
            client_socket.send(bytes('hi client'))                 #converyt string into byte in utf-8
        except:
            print("exited by the user")
    client_socket.close()
server_socket.close()