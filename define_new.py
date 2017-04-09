def fib(n):                                                                                        # 0
    '''accept an integer n.                                                                        # 1
    return the numbers less than n in Fibonacci sequence'''                                        # 2
    a, b = 1, 1                                                                                    # 3
    while a < n:                                                                                   # 4
        print(a, end=' ')                                                                          # 5
        a, b = b, a+b                                                                              # 6
    print()                                                                                        # 7
