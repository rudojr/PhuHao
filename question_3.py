import numpy as np

L = [[24,15,36], [81, 61, 10], [77,19,5]]
print("Ma trận:\n", np.array(L))
K = 2
r = np.array(L)[..., K-1]
print("Cột thứ 2 của ma trận:" + str(r))