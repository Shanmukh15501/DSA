import asyncio
import time

# Simulate an async task (non-blocking)
async def say_hello(request_id):
    print(f"[Request {request_id}] Hello")
    await asyncio.sleep(10)  # Simulate async work
    print(f"[Request {request_id}] World")
    return f"[Request {request_id}] Async Done"

# Simulate a blocking task (e.g., CPU or I/O bound)
def blocking_task(request_id):
    print(f"[Request Block {request_id}] Blocking task started")
    time.sleep(5)  # Simulate blocking work
    print(f"[Request {request_id}] Blocking task finished")
    return f"[Request {request_id}] Blocking Done"

# Each "request" runs both an async task and a blocking task
async def handle_request(request_id):
    async_part = say_hello(request_id)
    loop = asyncio.get_running_loop()
    blocking_part = loop.run_in_executor(None, blocking_task, request_id)
    results = await asyncio.gather(async_part, blocking_part)
    print(f"[Request {request_id}] Results: {results}")
    return results

# Main event loop running 3 concurrent requests
async def main():
    await asyncio.gather(
        handle_request(1),
        handle_request(2),
        handle_request(3),
    )

if __name__ == '__main__':
    asyncio.run(main())
