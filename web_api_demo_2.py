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

    await res # await last created task
    # this leads to non deterministic behaviour, because
    # the tasks are created in order, but not neccessarily
    # scheduled in order of creation by the event loop

    for i, task in enumerate(tasks):   # print numbered result in order
        try:    # necessary because not all tasks might have a result
            print(f'{i}: {task.result()}')
        except Exception as e:
            continue

    end_time = perf_counter()
    print(f'Elapsed time: {end_time - start_time:.2f} seconds')

if __name__ == "__main__":
    asyncio.run(main()) # run async main coroutine
