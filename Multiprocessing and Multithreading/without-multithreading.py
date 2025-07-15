### Multithreading
# first of all, we should know, when to use multithreading
# in I/O bound tasks: the program waits for an I/O task to get completed. Until it is not completed, the program cannot move on to do the next task. 
# the I/O task may include: reading through huge amount of files, or awaiting response from a network


# also in concurent execution: that is, when you want to increase your program's throughput, by increasing the no of tasks it can carry out simultaneously

import threading
import time


def print_numbers():
    for i in range(5):
        time.sleep(2)     # making the loop pause for 2s before moving to next, meaning, it will print 0, then  wait 2s, and then print 1, and so on
        print(f"Number: {i}")


def print_letters():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")


start_time=time.time()  # gets the time at the start of the execution of function
print_numbers()
print_letters()

end_time=time.time()-start_time  # gets the time at the end of function executions

print(f"Program Execution time: {end_time}")


# in this program you can see that, the numbers are printed with a 2sec interval
# and only after the print_numbers() execution is complete we are able to move on to the print_letters() execution
# this is what happens in single thread.

# now if you execute this code, the output will be like,
# Number: 0
# Number: 1
# Number: 2
# Number: 3
# Number: 4
# Letter: a
# Letter: b
# Letter: c
# Letter: d
# Letter: e
# Program Execution time: 20.009999752044678