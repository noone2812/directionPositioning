#!/usr/bin/env python3

import socket
import threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.data = ""
        self.startServer()

    def startServer(self):
        self.server.bind((self.host, self.port))
        self.server.listen()

        while True:
            connection, address = self.server.accept()
            new_thread = threading.Thread(target=new_node, args=(connection,))
            new_thread.start()

    def newNode(self):
        while True:
            self.data = self.server.recv(1024).decode()

            if not data:
                break
    
    def getData(self):
        return self.data

host = "0.0.0.0"
port = 5000
s = server(host, port)
