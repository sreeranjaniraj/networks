from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ("The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()  
    sentence = connectionSocket.recv(1024)  
    print("Server is started.")
    f = open(sentence,'rb')
    l = f.read(2048)
    while (l):
        print ('Sending...')
        connectionSocket.send(l)
        l = f.read(2048)
    print ("Done Sending")

            
