import socket
import sys


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    '''socket: This refers to the socket module in Python, 
          which provides a way to work with sockets and network communication'''
    '''.socket(): This is a constructor method provided by the socket module to create a socket object.'''
    '''socket.AF_INET: This is a constant that represents the address family, specifically IPv4. 
         It tells the socket that you'll be using the IPv4 addressing scheme.'''
    '''socket.SOCK_STREAM: This is a constant that represents the socket type. 
        SOCK_STREAM indicates that you want to create a TCP socket, which is a reliable, 
            connection-oriented socket used for streaming data.'''


except socket.error as e:
    print("Failed to create socket")
    print("Reason" + str(e))
    sys.exit()
print("socket created")
'''except socket.error as e:: This line initiates an exception handling block. 
       If an exception of type socket.error (which is a general exception class for socket-related errors) is raised 
        during the execution of the code in the try block (not shown in the provided code), 
        the code within this except block will be executed.'''

'''print("Failed to create socket"): If a socket error occurs, 
     this line prints an error message indicating that the socket creation has failed.'''

'''print("Reason" + str(e)): This line prints the reason for the error. 
   The variable e holds the exception object that was caught, and using str(e) 
    converts the exception object to a string so it can be displayed.'''

'''sys.exit(): This line terminates the program immediately. It's used to exit the script if a socket error occurs, 
   preventing the rest of the code from being executed.'''

'''print("socket created"): If no exception is raised and the socket creation is successful, 
   this line will be executed and it will print "socket created".'''
'''The purpose of this code structure is to handle any potential errors that might occur during socket creation 
   using the try and except blocks. If an error occurs, the error message and reason are printed, and the script exits.
    If there are no errors, the success message is printed. Remember, for this code to work, you need to have the 
    necessary imports (import socket and import sys) at the beginning of your script.'''
target_host = input("Enter the target host name to connect: ")
target_port = input("Enter the target port: ")
try:
    sock.connect((target_host, int(target_port)))
    print("socket connected to : " + target_host + target_port)
    sock.shutdown(2)
    '''try:: This line initiates a try block, indicating that the code inside this block might raise exceptions, 
        and you want to handle those exceptions.'''
    '''sock.connect((target_host, int(target_port))): This line attempts to establish a connection to the target host 
       and port. The sock variable is presumably a socket object created earlier using socket.socket(socket.AF_INET, 
       socket.SOCK_STREAM). The connect method is used to initiate a connection to the specified address (host and port)
       . target_host and target_port should be variables that hold the target host name or IP address and the port 
        number as strings. The int(target_port) converts the target_port to an integer before passing it to the 
        connect method.'''
    '''print("socket connected to : " + target_host + target_port): If the connection is successfully established, 
       this line prints a message indicating that the socket has been connected to the target host and port. However, 
       there's a mistake in this line. You need to concatenate the target_host and target_port values properly, 
       like this:

python
Copy code
print("socket connected to : " + target_host + ":" + target_port)'''
    '''sock.shutdown(2): This line initiates a graceful shutdown of the socket. The argument 2 indicates that both 
        sending and receiving operations will be disabled. This is often used to signal that you're done using the 
         socket.'''
except socket.error as err:
    '''
I see that you're referring to the socket.error part in your code. However, in modern versions of Python (3.x),
 the socket.error exception has been replaced with the more specific OSError exception when dealing with 
 socket-related errors'''
    print("Failed to connect :" + target_host + target_port)
    print("reason" + str(err))
    sys.exit()
    '''except socket.error as err:: This line initiates an exception handling block specifically for handling 
      socket.error exceptions, which are exceptions related to socket operations'''
    '''print("Failed to connect:" + target_host + target_port): If a socket.error exception occurs (indicating a failure
     to connect), this line prints an error message indicating that the connection attempt has failed. However, 
     there's a concatenation mistake in this line. You should concatenate the target_host and target_port 
     values properly, like this'''
    '''print("reason" + str(err)): This line prints the reason for the connection failure. The variable err holds 
       the exception object that was caught, and str(err) converts the exception object to a string so it can be 
       displayed'''
    '''sys.exit(): This line exits the script immediately if an exception occurs. It's used to terminate the script 
         after encountering an error'''