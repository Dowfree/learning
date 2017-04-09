def demo(s):
    result = [0, 0]
    for ch in s:
        if ch.isupper():
            result[0] += 1
        if ch.islower():
            result[1] += 1
    return tuple(result)

print(demo('dasdasdA'))