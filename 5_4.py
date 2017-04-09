def demo(lst, k):
    x = lst[:k]
    x.reverse()
    y = lst[k:]
    y.reverse()
    result = x+y
    result.reverse()
    return result

lst = list(range(1, 21))
print(lst)
print(demo(lst, 4))