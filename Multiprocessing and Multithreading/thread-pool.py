### Multithreading with thread pool executor
from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(numbers):
    time.sleep(1)
    return f"Number: {numbers}"
    

numbers=[1,2,3,4,5]

with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_numbers,numbers)


for i in results:
    print(i)