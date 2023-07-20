from utils import http_get_random_chuck, aio_http_get_random_chuck
from time import perf_counter
import asyncio  # import asyncio to run async methods

url = 'https://api.chucknorris.io/jokes/random?category=science' # url jokes

async def main():
    start_time = perf_counter()

    tasks = []
    for i in range(10):
        res = asyncio.create_task(aio_http_get_random_chuck(url))    # async wrapper method to retrieve jokes
        tasks.append(res)

    results = await asyncio.gather(*tasks) # await all created tasks 
    # await the result of multiple tasks at once using the gather method

    for i, task in enumerate(results):   # print numbered result in order
       print(f'{i}: {task}') # just strings, all tasks were awaited

    end_time = perf_counter()
    print(f'Elapsed time: {end_time - start_time:.2f} seconds')

if __name__ == "__main__":
    asyncio.run(main()) # run async main coroutine
