# here we are going to implement a real world example using logging, multi loggers
import logging

logging.basicConfig(
    level=logging.DEBUG,
    datefmt="%Y-%M-%D %H:%M:%S",
    filename="app1.log",
    filemode="w"
)

logger1=logging.getLogger("ArithmeticApp") # this will be my logger for this current application

def add(num1,num2):
    result=num1+num2
    logger1.debug(f"Adding {num1}+{num2} = {result}")
    return result


def sub(num1,num2):
    result=num1-num2
    logger1.debug(f"Subtracting {num1}-{num2} = {result}")
    return result

def mul(num1,num2):
    result=num1*num2
    logger1.debug(f"Multiplying {num1}*{num2} = {result}")
    return result

def div(num1,num2):
    try:
        result=num1/num2
        logger1.debug(f"Dividing {num1}/{num2} = {result}")
        return result
    except ZeroDivisionError:
        logger1.error("Division by 0 is not possible")
        return None
    

add(10,15)
sub(12,5)
mul(7,7)
div(70,5)
div(8,0)