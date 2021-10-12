import threading


class acquire(object):
    def __init__(self, *locks):
        self.locks = sorted(locks, key=lambda x: id(x))

    def __enter__(self):
        for lock in self.locks:
            lock.acquire()

    def __exit__(self, ty, val, tb):
        for lock in reversed(self.locks):
            lock.release()
        return False


# The philosopher thread
def philosopher(left, right):
    while True:
        with acquire(left, right):
            print(f"Philosopher at {threading.currentThread()} is eating.")


# The chopsticks
N_FORKS = 5
forks = [threading.Lock() for n in range(N_FORKS)]

# Create all of the philosophers
phils = [
    threading.Thread(target=philosopher, args=(forks[n], forks[(n + 1) % N_FORKS]))
    for n in range(N_FORKS)
]

# Run all of the philosophers
for p in phils:
    p.start()
