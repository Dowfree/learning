def demo(m, n):
    if m > 0 and n > 0:
        if m > n:
            m, n = n, m
        p = m*n
        while m != 0:
            r = n % m
            n = m
            m = r
        return n, int(p/n)
    else:
        raise ValueError("Please input two positive integers")

print(demo(-3, 30))
