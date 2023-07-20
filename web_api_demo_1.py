from utils import http_get_random_chuck, aio_http_get_random_chuck
from time import perf_counter
import asyncio  # import asyncio to run async methods

url = 'https://api.chucknorris.io/jokes/random?category=science' # url jokes

async def main():
    start_time = perf_counter()

    for i in range(10):
        res = await aio_http_get_random_chuck(url)    # async wrapper method to retrieve jokes
        print(f'{i}: {res}')    # print numbered result
        # This runs just link synchronous, blocking code
    end_time = perf_counter()
    print(f'Elapsed time: {end_time - start_time:.2f} seconds')

if __name__ == "__main__":
    asyncio.run(main()) # run async main coroutine
