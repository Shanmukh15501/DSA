import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

def cpu_bound_task(name, n):
    """Simulate CPU-heavy work (factorial calculation)"""
    print(f"{name} started (in process)")
    result = 1
    for i in range(1, n):
        result *= i  # heavy calculation
    print(f"{name} finished")
    return f"{name} done"

async def main():
    loop = asyncio.get_running_loop()

    # Create a process pool with 3 workers
    with ProcessPoolExecutor(max_workers=3) as pool:
        results = await asyncio.gather(
            loop.run_in_executor(pool, cpu_bound_task, "Task-1", 50_000),
            loop.run_in_executor(pool, cpu_bound_task, "Task-2", 10000),
            loop.run_in_executor(pool, cpu_bound_task, "Task-3", 70_000),
        )
    print("Results:", results)

if __name__ == "__main__":
    asyncio.run(main())
