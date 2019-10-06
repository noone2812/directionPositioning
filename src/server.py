#!/usr/bin/env python3
import numpy as np
import socket
import threading

class DataNode:
    def __init__(self, id, position):
        self.id = 0
        self.position = 0
        self.data = []
        self.online = True


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.data = ""

    def startServer(self, nodes):
        self.server.bind((self.host, self.port))
        self.server.listen()

        while True:
            connection, address = self.server.accept()
            new_thread = threading.Thread(target=new_node(nodes), args=(connection,))
            new_thread.start()

    def newNode(self, nodes):
        while True:
            self.data = self.server.recv(1024).decode()
            splitData = data.split[";"]
            if splitData[0] == "init" and sum([0] + [node.id == int(splitData[1] for node in nodes])) == 0:
                nodes.append(DataNode(id=int(splitData[1]),
                                position=np.array([float(splitData[2]), float(splitData[3])])))
            if not data:
                break
