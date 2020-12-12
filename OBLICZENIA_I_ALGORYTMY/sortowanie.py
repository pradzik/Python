from random import seed
from random import randint

int_list = []

for i in range(50):
    int_list.append(randint(0, 100))

for i in range(49):
    for j in range(49-i):
        if int_list[j] < int_list[j + 1]:
            int_list[j], int_list[j + 1] = int_list[j + 1], int_list[j]


for i in range(50):
    print(int_list[i])
