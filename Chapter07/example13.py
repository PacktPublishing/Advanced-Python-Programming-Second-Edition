import asyncio
import requests
from concurrent.futures import ThreadPoolExecutor


async def fetch_urls(urls):
    responses = []
    for url in urls:
        responses.append(await loop.run_in_executor(executor, requests.get, url))
    return responses


if __name__ == "__main__":
    executor = ThreadPoolExecutor(max_workers=3)
    loop = asyncio.get_event_loop()

    responses = loop.run_until_complete(
        fetch_urls(
            [
                "http://www.google.com",
                "http://www.example.com",
                "http://www.facebook.com",
            ]
        )
    )

    print(responses)
