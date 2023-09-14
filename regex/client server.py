import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server's address and port
server_address = ('192.168.0.108', 12345)
client_socket.connect(server_address)

# Send data to the server
message = "Hello, server! How are you?"
client_socket.send(message.encode('utf-8'))

# Receive a response from the server
response = client_socket.recv(1024)
print(f"Received from server: {response.decode('utf-8')}")

# Close the client socket
client_socket.close()

