from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
while 1:
    sentence, clientAddress = serverSocket.recvfrom(1024)
    k=0
    print("Server is started.")
    print("Press q to exit from server.")
    while 1: 
        if(k!=0):
            sentence, clientAddress = serverSocket.recvfrom(1024)   
        k+=1     
        print("Received from client:")
        print(sentence.decode())
        inp=input("Input msg from the server:")
        if(inp=='q'):
        	break
        else:
            serverSocket.sendto(inp.encode(), clientAddress)



            
