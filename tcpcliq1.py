from socket import *
import csv
from csv import writer
sum1=0
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input("Input file name:")
clientSocket.send(sentence.encode())

print("Receiving#...")
f = open('recvd.txt','wb')
l= clientSocket.recv(3000)
try:
    while (l):
        print ("Receiving...")
        f.write(l)
        clientSocket.settimeout(2)
        l,a = clientSocket.recv(3000)
except timeout:
    f.close()
    print ("File Downloaded")



