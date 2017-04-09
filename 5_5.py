def demo(t):
    a, b = 1, 1
    while b <= t:
        a, b = b, a+b
    return b

print(demo(50))
