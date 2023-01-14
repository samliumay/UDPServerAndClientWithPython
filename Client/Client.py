#In this aplication we will:
#Reads line of charachters (data) from its keyboard and sends data to server
#Sever recives the data and converts charachters to uppercase
#Server sends modified data to client
#Client recives the modified data and displays on its screen

from socket import *

nameOfServer = 'hostName'

#Means we will use specifically internet socket and UDP.
clientSocket = socket(AF_INET, SOCK_DGRAM)

print('Enter the message you will send:')
messageWeWillSend = input()
clientSocket.sendto(messageWeWillSend.encode(), ('127.0.0.1', 12000))

modifiedMassage, serverAdress = clientSocket.recvfrom(2048)

print( "Modified Massage is: " + modifiedMassage.decode())
clientSocket.close()
