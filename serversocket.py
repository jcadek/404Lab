#!/usr/bin/env python
# Copyright (c) James Cadek

import socket, os, sys, select

# Specifies TCP & IP
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
serverSocket.bind(("0.0.0.0",12347))

serverSocket.listen(5)

while True:
    print "Waiting for conection..."
    (incomingSocket, address) = serverSocket.accept()
    print "We got a connection from %s" % (str(address))
    pid = os.fork()
    if (pid == 0):
            #Child process
            outgoingSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            

            outgoingSocket.connect(("www.google.com",80))

        
            request = bytearray()
            while True:
                incomingSocket.setblocking(0)
                try:
                    part = incomingSocket.recv(1024)
                except socket.error as exception:
                    if exception.errno == 11:
                        part = None
                    else:
                        raise
                if(part):
                    request.extend(part)
                    outgoingSocket.sendall(part)
                
                outgoingSocket.setblocking(0)
                try:
                    part = outgoingSocket.recv(1024)
                except socket.error as exception:
                    if exception.errno == 11:
                        part = None
                    else:
                        raise
                if(part):
                    incomingSocket.sendall(part)
                select.select(
                        [incomingSocket, outgoingSocket],[],[incomingSocket, outgoingSocket],1000.0)
                
            print request
            sys.exit(0)


    else:
            #Parent process
            pass
    
