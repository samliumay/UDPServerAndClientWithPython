#In this aplication we will:
#Reads line of charachters (data) from its keyboard and sends data to server
#Sever recives the data and converts charachters to uppercase
#Server sends modified data to client
#Client recives the modified data and displays on its screen

from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(("127.0.0.1", serverPort))
print('The server is ready to service')

while True:
    message, clientAdress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAdress)

