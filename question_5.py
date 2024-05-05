import numpy as np

p = 121
p1 = np.array((1, 1, 1))
p2 = np.array((1, 2, 3))

print(np.sqrt(p))
print(np.dot(p1, p2))
print(np.square(p1 - p2))

kc = np.linalg.norm(p1 - p2)
print(kc)