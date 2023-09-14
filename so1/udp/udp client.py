import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = 'hello udp fine'
client_socket.sendto(msg.encode('utf-8'), ('192.168.0.108', 456))
data, addr = client_socket.recvfrom(4096)
print('server says')
client_socket.close()
