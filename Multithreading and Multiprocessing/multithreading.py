### Multithreading
## When to use Multi Threading
###I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests).
###  Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")

def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
# Start threads
thread1.start()
thread2.start()
# Join threads
thread1.join()
thread2.join()


start_time = time.time()
# print_numbers()
# print_letters() 
end_time = time.time()
print(f"Time taken: {end_time - start_time}")