import aiohttp
import aiofiles
import asyncio

import os
from timeit import default_timer as timer


async def download_html(session, url):
    async with session.get(url, ssl=False) as res:
        filename = "output/%s.html" % os.path.basename(url)

        async with aiofiles.open(filename, "wb") as f:
            while True:
                chunk = await res.content.read(1024)
                if not chunk:
                    break
                await f.write(chunk)

        return await res.release()


async def main(url):
    async with aiohttp.ClientSession() as session:
        await download_html(session, url)


urls = [
    "http://packtpub.com",
    "http://python.org",
    "http://docs.python.org/3/library/asyncio",
    "http://aiohttp.readthedocs.io",
    "http://google.com",
]

start = timer()

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*(main(url) for url in urls)))

print("Took %.2f seconds." % (timer() - start))
