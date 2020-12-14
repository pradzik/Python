import threading
import random
import time


class Philosopher(threading.Thread):
    flag_if_eating = True

    def __init__(self, ID, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.ID = ID
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while self.flag_if_eating:
            time.sleep(10)
            print(f"Philosopher {self.ID} is hungry.")
            self.dine()

    def dine(self):
        while self.flag_if_eating:
            self.left_fork.acquire()
            locked = self.right_fork.acquire(False)
            if locked:
                break
            self.left_fork.release()
            print(f"Philosopher {self.ID} swaps forks.")
            self.left_fork, self.right_fork = self.right_fork, self.left_fork
        else:
            return
        self.dining()
        self.right_fork.release()
        self.left_fork.release()

    def dining(self):
        print(f"Philosopher {self.ID} is going to eat")
        time.sleep(10)
        print(f"Philosopher {self.ID} finishes eating and leaves to think.")


forks = [threading.Semaphore() for n in range(5)]
philosophers = [Philosopher(i, forks[i % 5], forks[(i + 1) % 5]) for i in range(5)]
Philosopher.flag_if_eating = True
for p in philosophers:
    p.start()
time.sleep(30)
Philosopher.flag_if_eating = False
print("All philosopher are all full")
