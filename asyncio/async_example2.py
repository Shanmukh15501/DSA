import asyncio
import subprocess
import sys
import time
async def say_hello():
    start =  time.time()
    print("Hello")
    await asyncio.sleep(10)   # non-blocking sleep
    # time.sleep(10) #blocking operation
    print("World")
    return time.time() - start

async def main():
    start = time.time()
    results = await asyncio.gather(
        say_hello(),
        say_hello(),
        say_hello(),
    )
    print(f"Execution times: {results}")
    print("Total Time",time.time() - start) 
    

if __name__ == '__main__':
    asyncio.run(main())