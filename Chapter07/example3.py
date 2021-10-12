import threading


def network_request_async(number, on_done):
    def timer_done():
        on_done({"success": True, "result": number ** 2})

    timer = threading.Timer(1.0, timer_done)
    timer.start()


def fetch_square(number):
    def on_done(response):
        if response["success"]:
            print("Result is: {}".format(response["result"]))

    network_request_async(number, on_done)


def on_done(result):
    print(result)


if __name__ == "__main__":
    ### First discussion
    network_request_async(2, on_done)

    ### Second discussion
    # network_request_async(2, on_done)
    # network_request_async(3, on_done)
    # network_request_async(4, on_done)
    # print("After submission")

    ### Third discussion
    # fetch_square(2)
    # fetch_square(3)
    # fetch_square(4)
