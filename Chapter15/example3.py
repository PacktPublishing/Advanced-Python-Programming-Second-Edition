import time
import threading
from multiprocessing import Pool

COUNT = 50000000


def countdown(n):
    while n > 0:
        n -= 1


if __name__ == "__main__":

    #######################################################################
    # Sequential

    start = time.time()
    countdown(COUNT)

    print("Sequential program finished.")
    print(f"Took {time.time() - start : .2f} seconds.")
    print()

    #######################################################################
    # Multithreading

    thread1 = threading.Thread(target=countdown, args=(COUNT // 2,))
    thread2 = threading.Thread(target=countdown, args=(COUNT // 2,))

    start = time.time()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    print("Multithreading program finished.")
    print(f"Took {time.time() - start : .2f} seconds.")
    print()

    #######################################################################
    # Multiprocessing

    pool = Pool(processes=2)
    start = time.time()
    pool.apply_async(countdown, args=(COUNT // 2,))
    pool.apply_async(countdown, args=(COUNT // 2,))
    pool.close()
    pool.join()

    print("Multiprocessing program finished.")
    print(f"Took {time.time() - start : .2f} seconds.")
