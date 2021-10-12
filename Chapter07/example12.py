import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


executor = ThreadPoolExecutor(max_workers=3)


def wait_and_return(msg):
    time.sleep(1)
    return msg


### First example
# print(executor.submit(wait_and_return, "Hello. executor"))

### Second example
loop = asyncio.get_event_loop()
fut = loop.run_in_executor(executor, wait_and_return, "Hello, asyncio executor")
print(fut)
print(loop.run_until_complete(fut))
