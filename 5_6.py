def demo(lst):
    m = min(lst)
    result = (m,)
    for i in range(len(lst)):
        if lst[i] == m:
            result += (i,)
    """
    other solution:
        for index, value in enumerate(lst):
            if value == m:
                result += (index,)

    """
    return result


print(demo([1, 2, 1, 3, 1, 4, 1, 5]))
