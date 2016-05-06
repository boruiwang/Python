#!/usr/bin/python           
# This is server.py file
from threading import *
import socket, thread, sys
def f(sock):
    # close parent socket
    #sock.close()
    connection.send("Welcome to Borui's Chat Room")
    while True:
        data = connection.recv(1024)
        if data == 'client disconnect':
            print 'clinet disconnect'
            thread.exit()
        else:
            print '<clinet1> %s' % data

if __name__ == '__main__':
    # Create a TCP/IP socket
    sock = socket.socket()
    host = ''
    port = 12345
    print 'starting up on %s port %s' % (host, port)
    sock.bind((host, port))
    # Listen for incoming connections
    sock.listen(1)
    # Wait for a connection
    while True:
        print 'waiting for a connection'
        connection, client_address = sock.accept()
        print 'connection from', client_address

        p = Thread(target=f, args=(sock,))
        p.start()

  
    sock.close()