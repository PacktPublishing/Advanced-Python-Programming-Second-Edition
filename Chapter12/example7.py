import threading
import time
from timeit import default_timer as timer


def thread_a():
    print("Thread A is starting...")

    print("Thread A is performing some calculation...")
    time.sleep(2)

    print("Thread A is performing some calculation...")
    time.sleep(2)


def thread_b():
    print("Thread B is starting...")

    print("Thread B is performing some calculation...")
    time.sleep(5)

    print("Thread B is performing some calculation...")
    time.sleep(5)


thread1 = threading.Thread(target=thread_a)
thread2 = threading.Thread(target=thread_b)

start = timer()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Took %.2f seconds." % (timer() - start))

print("Finished.")
