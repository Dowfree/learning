import math


def IsPrime(n):
    m = int(math.sqrt(n)) + 1
    for i in range(2, m):
        if n % i == 0:
            return False
    return True


def demo(n):
    if isinstance(n, int) and n > 0 and n % 2 == 0:
        for i in range(3, int(n/2)+1):
            if IsPrime(i) and IsPrime(n-i):
                print(i, '+', n-i, '=', n)
    else:
        raise ValueError("Please input an positive even number")

demo(60)
