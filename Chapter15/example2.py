import time
import threading

COUNT = 50000000


def countdown(n):
    while n > 0:
        n -= 1


###########################################################################

start = time.time()
countdown(COUNT)

print("Sequential program finished.")
print(f"Took {time.time() - start : .2f} seconds.")

###########################################################################

thread1 = threading.Thread(target=countdown, args=(COUNT // 2,))
thread2 = threading.Thread(target=countdown, args=(COUNT // 2,))

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("Concurrent program finished.")
print(f"Took {time.time() - start : .2f} seconds.")
