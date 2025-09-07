import asyncio
import subprocess
import sys
import time
async def say_hello():
    start =  time.time()
    print("Hello")
    await asyncio.sleep(10)   # non-blocking sleep
    print("World")
    return ("Total Time",time.time() - start) 

    
async def main():
    results = await say_hello()
    print(f"Execution times: {results}")

if __name__ == '__main__':
    asyncio.run(main())
    
    
#Calling the function:
    #coro = say_hello()
    #This does not run the function immediately.
    #Instead, it creates and returns a coroutine object — a kind of "promise" to do the work later.
