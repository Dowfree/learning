def pingpong(n, k=7):
    if not isinstance(n, int) or n <= 0:
        raise TypeError("%s is not the correct index" % n)
    num, index, key = 0, 0, 1
    while index < n:
        num += key
        index += 1
        if str(k) in list(str(index)) or index % k == 0:
            key = -key
    return num

print(pingpong(0))
