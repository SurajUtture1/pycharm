import socket
addr = '127.9.00'

try:
    socket.inet_aton(addr)
    print("valid")
except socket.error:
    print("invalid")


