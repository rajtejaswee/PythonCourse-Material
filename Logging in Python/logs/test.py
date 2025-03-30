from logger import logging

def add(a, b):
    logging.debug("The addition aoperation is taking place")
    return a + b

logging.debug("The addition function is called")
add(12,23)