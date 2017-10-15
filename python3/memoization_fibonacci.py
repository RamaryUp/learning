'''
 Testing memoization using lru_cache against Fibonacci function
'''

import sys

from functools import lru_cache

@lru_cache()
def fibonacci(n):
    if type(n) != int:
        raise TypeError("n must be positive integer . Type is", type(n))
    elif n < 1:
        raise ValueError("n must be > 0")
    elif n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

def test_fibonacci():
    print("Starting Fibonacci program")
    print("Input an integer : ")
    
    text = input().strip()
    try:
        number = int(text)
    except:   
        print("Exception occured when converting input ExceptionType:{} Description:{}".format( sys.exc_info()[0], sys.exc_info()[1]))         
        return

    try:
        result = fibonacci(number)
    except:
        print("Exception occured ExceptionType:{} Description:{}".format( sys.exc_info()[0], sys.exc_info()[1]))
    else:
        print("Fibonacci({})={}".format(number, result))

if __name__ == "__main__" :
    test_fibonacci()