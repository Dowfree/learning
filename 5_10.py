def demo(x, n):
    if n not in x:
        raise ValueError("%d is not in list" %(n))
    less, greater = [], []
    for i in x:
        if i < n:
            less.append(i)
        elif i > n:
            greater.append(i)
    result = less+[n]+greater
    print(result)
    if len(result) == len(x):
        for i in range(len(x)):
            x[i] = result[i]
        return x
    else:
        raise ValueError("There are same numbers in list x")

x = [5, 4, 3, 2, 1, 6, 8, 7, 9]
demo(x, 5)
print(x)
