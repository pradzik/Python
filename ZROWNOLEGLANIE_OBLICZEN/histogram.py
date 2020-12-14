from random import randint
import threading
import matplotlib.pyplot as plt

data = []
y = []
p = []
x = list(range(0, 36))

for i in range(1800):
    data.append(randint(0, 2000))

lock = threading.Lock()


def threads_list(data, lock):
    lock.acquire()
    n = list()
    for j in range(6):
        n.append(0)

    for j in range(len(data)):
        if data[j] <= 300:
            n[0] += 1
        elif data[j] <= 600:
            n[1] += 1
        elif data[j] <= 900:
            n[2] += 1
        elif data[j] <= 1200:
            n[3] += 1
        elif data[j] <= 1500:
            n[4] += 1
        else:
            n[5] += 1

    for j in range(6):
        y.append(n[j])
    lock.release()


for i in range(6):
    p1 = threading.Thread(target=threads_list, args=(data, lock))
    p1.start()
    p1.join()

plt.hist(data, 20)
plt.show()

print(len(x))
print(y)
colors = ["orange"]*6 + ["purple"]*6 + ["darkturquoise"]*6+ ["firebrick"]*6 + ["limegreen"]*6 + ["red"]*6
barPlot = plt.bar(x, y, color=colors)
plt.show()