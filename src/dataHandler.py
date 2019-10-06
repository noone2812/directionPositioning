import numpy as np
import server.py

class DataNode:
    def __init__(self, id):
        self.id = 0
        self.position = [np.array([1, 2]), np.array([5, 9]), np.array([7, 4]), np.array([1, 1])][self.id]
        self.data = []
        self.online = False

class DataHandler:
    def __init__(self, server):
        self.server = server  
        self.nodes = []
    
    self.server.getData()
