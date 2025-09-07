from concurrent.futures import ProcessPoolExecutor
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)

def print_alphabets():
    for i in ['a', 'b', 'c', 'd', 'e']:
        time.sleep(1)
        print(i)


if __name__ == '__main__':
    start_time = time.time()    

    with ProcessPoolExecutor(max_workers=2) as executor:
        executor.submit(print_numbers)
        executor.submit(print_alphabets)

    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")