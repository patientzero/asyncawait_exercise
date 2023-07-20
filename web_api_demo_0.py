from utils import http_get_random_chuck
from time import perf_counter

url = 'https://api.chucknorris.io/jokes/random?category=science' # url jokes

def main():
    start_time = perf_counter() # get start time

    for i in range(10):
        res = http_get_random_chuck(url)    # wrapper method to retrieve jokes
        print(f'{i}: {res}')    # print numbered result

    end_time = perf_counter()   # get end time and calculate elapsed time
    print(f'Elapsed time: {end_time - start_time:.2f} seconds')

if __name__ == "__main__":
    main() # call main function
