import time
import threading
import asyncio
from concurrent.futures import ThreadPoolExecutor

def blocking_task(name):
    print(f"Starting blocking task {name} on {threading.current_thread().name}")
    time.sleep(5)
    print(f"Finished blocking task {name} on {threading.current_thread().name}")
    return name

async def main():
    start = time.time()

    # Create a ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=3) as executor:
        loop = asyncio.get_running_loop()
        tasks = [
            loop.run_in_executor(executor, blocking_task, "A"),
            loop.run_in_executor(executor, blocking_task, "B"),
            loop.run_in_executor(executor, blocking_task, "C"),
        ]
        results = await asyncio.gather(*tasks)

    print("Results:", results)
    print("Total Time:", time.time() - start)

asyncio.run(main())
