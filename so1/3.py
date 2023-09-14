# see the interaction between client and server
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.0.108', 12456))
pay_load = 'hi server'  # send the data to the server and receive the data from the server

try:
    while True:
        client_socket.send(pay_load.encode('utf-8'))  # send the data
        data = client_socket.recv(1024)  # receive the data and mention buffer size 1024
        print(str(data))
        more = input("send from user")
        if more.lower() == 'y':  # data convert into lower
            '''In this example, the code sends data to the server and receives a response. Then, it prompts the user 
            to input whether they want to send more data. If the user inputs "no", the loop breaks and the socket is closed. 
            You can expand the logic to handle different cases or perform various actions based on user input'''

            payload = input("enter payload")
        else:
            break
except KeyboardInterrupt:
    print("exited by user")
client_socket.close()

