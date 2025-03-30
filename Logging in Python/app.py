import logging

## logging setting

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)   

logger= logging.getLogger('ArithematicApp')

def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} and {b} gives {result}")
    return result
def subtract(a, b):   
    result = a - b
    logger.debug(f"Subtracting {b} from {a} gives {result}")
    return result
def multiply(a, b):
    result = a * b
    logger.debug(f"Multiplying {a} and {b} gives {result}")
    return result
def divide(a, b):       
    try:
        result = a/b
        logger.debug(f"Dividing {a} by {b} gives {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero is not allowed")
        return None
    
add(10, 5)
subtract(10, 2)
multiply(10, 5)
divide(10, 0)
divide(10, 2)