from concurrent.futures import ProcessPoolExecutor
import time
import os

def task1():
    print(f"Task 1 running in process ID: {os.getpid()}")
    for _ in range(10**8):
        pass
    print("Task 1 done")

def task2():
    print(f"Task 2 running in process ID: {os.getpid()}")
    for _ in range(10**8):
        pass
    print("Task 2 done")

def task3():
    print(f"Task 3 running in process ID: {os.getpid()}")
    for _ in range(10**8):
        pass
    print("Task 3 done")

def task4():
    print(f"Task 4 running in process ID: {os.getpid()}")
    for _ in range(10**8):
        pass
    print("Task 4 done")

def task5():
    print(f"Task 5 running in process ID: {os.getpid()}")
    for _ in range(10**8):
        pass
    print("Task 5 done")

if __name__ == '__main__':
    start_time = time.time()

    with ProcessPoolExecutor(max_workers=5) as executor:
        executor.submit(task1)
        executor.submit(task2)
        executor.submit(task3)
        executor.submit(task4)
        executor.submit(task5)

    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")
