from concurrent.futures import Future
import threading


def network_request_async(number):
    future = Future()
    result = {"success": True, "result": number ** 2}
    timer = threading.Timer(1.0, lambda: future.set_result(result))
    timer.start()

    return future


def fetch_square(number):
    fut = network_request_async(number)

    def on_done_future(future):
        response = future.result()
        if response["success"]:
            print("Result is: {}".format(response["result"]))

    fut.add_done_callback(on_done_future)


if __name__ == "__main__":
    ### First try
    fut = network_request_async(2)

    ### Second try
    # fetch_square(2)
