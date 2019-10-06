import numpy as np
import server.py

class DataHandler:
    def __init__(self, server):
        self.server = server
        self.nodes = []
        self.server.start_server(self.nodes)
    
    def run(self):
        while True:


    self.server.getData()

dh = DataHandler(Server(host="0.0.0.0", 
                        port=3000))
