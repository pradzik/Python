import numpy as np
from random import seed
from random import randint

matrix_size = int(randint(1, 5))
print(matrix_size)
x = np.empty((matrix_size, matrix_size))

for i in range(len(x)):
    for j in range(len(x)):
        x[i][j] = randint(1, 5)


det = np.linalg.det(x)
print(x)
print(det)