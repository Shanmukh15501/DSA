from concurrent.futures import ProcessPoolExecutor
import time

def cpu_bound():
    for i in range(10**8):
        pass
    print("Done")


if __name__ == '__main__':
    start_time = time.time()    

    with ProcessPoolExecutor(max_workers=2) as executor:
        executor.submit(cpu_bound)

    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")