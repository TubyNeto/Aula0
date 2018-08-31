import numpy as np

M=np.random.rand(3,3)
print(M)

np.save("saved-matrix.npy", M)
np.load("saved-matrix.npy")
