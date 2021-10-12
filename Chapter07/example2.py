import time
import threading


def wait_and_print(msg):
    time.sleep(1.0)
    print(msg)


def wait_and_print_async(msg):
    def callback():
        print(msg)

    timer = threading.Timer(1.0, callback)
    timer.start()


if __name__ == "__main__":
    wait_and_print("First call")
    wait_and_print("Second call")

    wait_and_print_async("First call async")
    wait_and_print_async("Second call async")
