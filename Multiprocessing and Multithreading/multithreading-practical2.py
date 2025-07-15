 # in this file, we will try to implement the multithreading, so that when print_numbers() function is sleeping, we may execute the print_letters(), and hence reducing execution time


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


# so now,we will create two threads
t1=threading.Thread(target=print_numbers)  # thread t1 will be responsible for execution of print_numbers
t2=threading.Thread(target=print_letters)  # thread t2 will be responsible for execution of print_letters


start_time=time.time()  

# and now instead of calling these functions, we will start the thread
t1.start()
t2.start()


# and once the execution of these threads are complete,they will be joined back to the main thread
t1.join()
t2.join()

end_time=time.time()-start_time  

print(f"Program Execution time: {end_time}")


# now if you execute this code, the output will be like,
# number: 0 
# letter : a
# number: 1
# letter: b
# number: 2
# letter: c
# number: 3
# letter: d
# number: 4
# letter: e
# Program execution time: 10.007002830505371 
# so you see that both functions are simultaneously executed, and the execution time is almost brought down to half   