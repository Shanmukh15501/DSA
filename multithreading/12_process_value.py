from multiprocessing import Process, Value, Queue

def increment(counter,q):
    for _ in range(100):
        lock = counter.get_lock()
        lock.acquire()
        counter.value += 1
        lock.release()
        q.put(counter.value)


if __name__ == "__main__":
    counter = Value('i', 0)
    q = Queue()
    processes = [Process(target=increment, args=(counter, q,)) for _ in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]

    print("Final counter value: ",counter.value )
    while not q.empty():
        print(q.get())

        
# all 4 run in parallel once lock is realized other process catches it 
#process 1 will lock → release → process 2 will start → release → process 3 → release → process 4 → release → then process 1 again …
#order might change based on os but increment with updated value happens 100000 times in each 