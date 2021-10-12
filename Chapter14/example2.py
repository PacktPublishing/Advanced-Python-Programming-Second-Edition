import threading
import random
import time


def update():
    global counter

    with count_lock:
        current_counter = counter  # reading in shared resource
        time.sleep(random.randint(0, 1))  # simulating heavy calculations
        counter = current_counter + 1


counter = 0
count_lock = threading.Lock()

threads = [threading.Thread(target=update) for i in range(20)]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(f"Final counter: {counter}.")
print("Finished.")
