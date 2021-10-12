import threading
import random

random.seed(0)
import time


def update(pause_period):
    global counter

    with count_lock:
        current_counter = counter  # reading in shared resource
        time.sleep(pause_period)  # simulating heavy calculations
        counter = current_counter + 1  # updating shared resource


pause_periods = [random.randint(0, 1) for i in range(20)]

###########################################################################

counter = 0
count_lock = threading.Lock()

start = time.perf_counter()
for i in range(20):
    update(pause_periods[i])

print("--Sequential version--")
print(f"Final counter: {counter}.")
print(f"Took {time.perf_counter() - start : .2f} seconds.")

###########################################################################

counter = 0

threads = [threading.Thread(target=update, args=(pause_periods[i],)) for i in range(20)]

start = time.perf_counter()
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("--Concurrent version--")
print(f"Final counter: {counter}.")
print(f"Took {time.perf_counter() - start : .2f} seconds.")

###########################################################################

print("Finished.")
