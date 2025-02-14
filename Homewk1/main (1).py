import random
import time

def decorator_1(func):
    
    def amount(*args, **kwargs):
        
        starting = time.perf_counter()
        func(*args, **kwargs)
        finishing  = time.perf_counter()
        duration = finishing - starting 
        
        print(f"{func.__name__} {duration:.6f} sec")
    return amount

@decorator_1

def func():
    
    print("I am ready to Start")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += (i**2)


@decorator_1

def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i


if name == "__main__":
    func()
    funx()
    func()
    funx()
    func()