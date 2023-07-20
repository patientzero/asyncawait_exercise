import asyncio
import aiohttp
import requests
import time


def http_get_random_chuck(url):
    try:
        res = requests.get(url)
        return res.json()['value']
    except Exception as e:
        time.sleep(0.123)
        return "Never gonna give you up"

async def aio_http_get_random_chuck(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as res:
                    tmp = await res.json()
                    return tmp['value']
    except Exception as e:
        await asyncio.sleep(0.2)
        return "Never gonna give you up"

async def async_http_get_random_chuck(url):
    res = await asyncio.to_thread(http_get_random_chuck, url)
    return res
