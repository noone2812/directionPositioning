import numpy as np

r1 = np.array([1, 2])
r2 = np.array([5, 9])
r3 = np.array([17, 40])
r  = np.array([100, 100])
s1 = (r - r1) / np.linalg.norm(r - r1)
s2 = (r - r2) / np.linalg.norm(r - r2)
s3 = (r - r3) / np.linalg.norm(r - r3)

print(s1)
print(s2)
    
def dirs2pos(dirs, nodeLocs):
    I = np.identity(dirs[0].shape[0])
    A = len(dirs) * I
    B = np.zeros(dirs[0].shape[0]).reshape(-1, 1)
    for direction, nodeLoc in zip(dirs, nodeLocs):
        A -= np.matmul(direction.reshape(-1, 1), direction.reshape(1, -1))
        B += np.matmul((I - np.matmul(direction.reshape(-1, 1), direction.reshape(1, -1))), nodeLoc.reshape(-1, 1))
    return np.matmul(np.linalg.inv(A), B)
print(dirs2pos([s1, s2], [r1, r2]))