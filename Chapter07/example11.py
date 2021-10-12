import asyncio


async def network_request(number):
    await asyncio.sleep(1.0)
    return {"success": True, "result": number ** 2}


async def fetch_square(number):
    response = await network_request(number)
    if response["success"]:
        print("Result is: {}".format(response["result"]))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    ### First example
    loop.run_until_complete(fetch_square(2))
    loop.run_until_complete(fetch_square(3))
    loop.run_until_complete(fetch_square(4))

    ### Second example
    # asyncio.ensure_future(fetch_square(2))
    # asyncio.ensure_future(fetch_square(3))
    # asyncio.ensure_future(fetch_square(4))
    # # Hit Ctrl-C to stop the loop
    # loop.run_forever()
