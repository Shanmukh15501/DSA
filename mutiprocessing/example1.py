import multiprocessing
import time

def print_numbers(n1,n2):
    for i in range(n1+n2):
        time.sleep(1)
        print(i)

def print_alphabets():
    for i in ['a', 'b', 'c', 'd', 'e']:
        time.sleep(1)
        print(i)

if __name__ == '__main__':
    start_time = time.time()

    # Create processes
    process1 = multiprocessing.Process(target=print_numbers, name="Process-1",args=(1,9))
    process2 = multiprocessing.Process(target=print_alphabets, name="Process-2")

    # Start processes
    process1.start()
    process2.start()

    # Wait for both to finish
    process1.join()
    process2.join()

    end_time = time.time()
    total_time = end_time - start_time

    print(f"Total execution time: {total_time:.2f} seconds")
