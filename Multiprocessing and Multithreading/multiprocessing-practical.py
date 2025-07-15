### what does multiprocessing allow us to do?
# multiprocessing allows us  to carry out parallel execution of processes

### when should we use multiprocessing?
# in case of CPU-bound tasks-> tasks which are very heavy on CPU usage
# when we want to carry out parallel execution of processes, utilizing more CPU cores at once

import multiprocessing
import time


# this function will be pausing for 1 second after every loop
def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")



# this function will be pausing for 1.5 seconds after every loop
def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i*i*i}")

if __name__=="__main__":
    # now instead of calling these functions, we will create processes
    p1=multiprocessing.Process(target=square_numbers)

    p2=multiprocessing.Process(target=cube_numbers)
    start_time=time.time()


    # and then we'll start these processes
    p1.start()
    p2.start()


    # and finally we'll wait for these processes to end, and join with the main process
    p1.join()

    p2.join()


    exec_time=time.time()-start_time 
    print(f"Execution time: {exec_time}")


# it may seem similar to multithreading, but its not
# in this case, two processes will be created and you may observe it from the task manager as well
# the output will be
# Square: 0
# Cube: 0
# Square: 1
# Square: 4
# Cube: 1
# Square: 9
# Cube: 8
# Square: 16
# Cube: 27
# Cube: 64
# Execution time: 7.648998975753784