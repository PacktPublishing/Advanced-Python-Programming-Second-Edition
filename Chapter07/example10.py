import asyncio


async def wait_and_print(msg):
    await asyncio.sleep(1)
    print("Message: ", msg)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(wait_and_print("Hello"))
