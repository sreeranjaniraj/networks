from socket import *
serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.connect((serverName,serverPort))
print ("Client is started.")
print ("Press q to exit from server.")

#sentence = input("Input sentence from the client:")
while(True):
    sentence = input("Input sentence from the client:")
    if(sentence=='q'):
        break
    else:
        clientSocket.sendto(sentence.encode(), (serverName, serverPort))
        modifiedSentence, serverAddress = clientSocket.recvfrom(1024)
        print ("Received from Server:", modifiedSentence.decode())





        
	    


