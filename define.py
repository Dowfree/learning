def fib(n):
    '''accept an integer n.
    return the numbers less than n in Fibonacci sequence'''
    a, b = 1, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
