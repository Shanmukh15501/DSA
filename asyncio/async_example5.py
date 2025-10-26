import asyncio
import time
import threading

def blocking_task(name):
    print(f"Starting blocking task {name} on {threading.current_thread().name}")
    time.sleep(5)  # Simulate blocking operation
    print(f"Finished blocking task {name} on {threading.current_thread().name}")
    return name

async def main():
    start = time.time()

    # Run blocking functions in separate threads (non-blocking for async)
    results = await asyncio.gather(
        asyncio.to_thread(blocking_task, "A"),
        asyncio.to_thread(blocking_task, "B"),
        asyncio.to_thread(blocking_task, "C"),
    )

    print("Results:", results)
    print("Total Time:", time.time() - start)

asyncio.run(main())
