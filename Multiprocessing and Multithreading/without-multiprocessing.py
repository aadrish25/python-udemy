

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


start_time=time.time()
square_numbers()
cube_numbers()
exec_time=time.time()-start_time
print(f"Execution time: {exec_time}")


# Output and execution time of this program:
# Square: 0
# Square: 1
# Square: 4
# Square: 9
# Square: 16
# Cube: 0
# Cube: 1
# Cube: 8
# Cube: 27
# Cube: 64
# Execution time: 12.510000467300415