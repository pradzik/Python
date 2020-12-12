import numpy as np
from random import seed
from random import randint

x = np.empty((8, 8))
y = np.empty((8, 8))
z = np.zeros((8, 8))

for i in range(len(x)):
    for j in range(len(x)):
        x[i][j] = randint(1, 2)
        y[i][j] = randint(1, 2)

for i in range(len(x)):  # iterate through row of x
    for j in range(8):  # iterate through columns of y
        for k in range(len(y)):  # iterate through rows of y
            z[i][j] += x[i][k] * y[k][j]


print("X= ", x[0, :])
print("Y= ", y[:, 0])
print("Z= ", z[0][0])
