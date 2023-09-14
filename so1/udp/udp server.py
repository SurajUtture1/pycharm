'''it is connectionless software that is client not have connection with client and server
    client sends a datagram and server not accept a connection and just waits for datagram to arrive aand datagram aontains address of sender
    and which server used to send a data to the correct client
       udp doesnot check for  arrive in the exchange data thats y it gives a fast communication it is similar to TCP
    and changes are there
1. once after creating socket object server process bind that socket to perticular ip address and port number and
  after binding server process start waiting untill datagram packet arrive from client
2. after binding UDP enter into the request and reply infinite loop when cloent finishes the process and exit by close
   the connection and at that time server process probably go to the waiting list and'''

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('192.168.0.108', 123))
while True:
    data, addr = sock.recvfrom(4096)    # data in the form of bites 4096
    print(str(data))
    message = bytes("hello i am udp").encode('utf-8')
    sock.sendto(message, addr)
