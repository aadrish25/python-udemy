### multiprocessing usecase
# used in factorial calculation of large numbers
# factorial calculation of very large numbers, might be heavy load for a single CPU core
# multiprocessign allows us to distribute the workload across multiple CPU cores, improving performance

import multiprocessing
import math
import sys


sys.set_int_max_str_digits(1000000) # increase maximum no of digits for integer conversion

numbers=[100,500,1000,10000] # we'll take factorial of these large numbers


# function to get the factorial
def get_factorial(number):
    factorial=math.factorial(number)
    print(f"Factorial of {number}: {factorial}")
    return factorial


# now we'll create an empty list where we store the processes
processes=[]

if __name__=="__main__":
    # and then create a separate process for factorial calculation of each number
    # then appending the process to the processes list
    # then starting the process
    for num in numbers:
        process=multiprocessing.Process(target=get_factorial,args=(num,))
        processes.append(process)
        process.start()

    # then we wait for the processes to finish, and join with the main process
    for process in processes:
        process.join()


    print("Execution complete")
