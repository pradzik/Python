import numpy as np
from random import seed
from random import randint

x = np.empty((128, 128))
y = np.empty((128, 128))

for i in range(len(x)):
    for j in range(len(x)):
        x[i][j] = randint(1, 50)
        y[i][j] = randint(1, 50)

z = x + y

print(x[1][1], y[1][1], z[1][1])