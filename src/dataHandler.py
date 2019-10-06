import numpy as np

class DataNode:
    def __init__(self, id):
        self.id = 0
        self.position = [np.array([1, 2]), np.array([5, 9])][self.id]
        self.data = []
        self.online = False

class DataHandler:
    def __init__(self, server):
        self.server = server  
        self.nodes = []
