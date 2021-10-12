import time


def network_request(number):
    time.sleep(1.0)
    return {"success": True, "result": number ** 2}


def fetch_square(number):
    response = network_request(number)
    if response["success"]:
        print("Result is: {}".format(response["result"]))


if __name__ == "__main__":
    fetch_square(2)
    fetch_square(3)
    fetch_square(4)
