#!/usr/bin/env python3

def print_fibonacci(length):
    fib = []
    if length == 0:
        print(fib)
    elif length == 1:
        fib.append(0)
        print(fib)
    elif length == 2:
        fib.append(0)
        fib.append(1)
        print(fib)
    else: 
        fib = [0, 1]
        for n in range(2, length):
            next = fib[-1] + fib[-2]
            fib.append(next)
            
        print(fib)
    pass