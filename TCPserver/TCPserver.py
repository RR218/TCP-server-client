#!/usr/bin/env python3

import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = input("Please specify the port number: ")

serverSocket.bind((host, port))

serverSocket.listen(3)

while True:
    clientSocket, address = serverSocket

    print("received connection form %s" % str(address))

    message = "server connected" + "\r\n"

    clientSocket.send(message.encode("ascii"))

    clientSocket.close()
