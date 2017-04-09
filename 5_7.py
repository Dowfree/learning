def demo(t):
    result = [[1]] * t
    print(result[1])
    for i in range(1, t):
        result[i] = [1] * (i+1)
        for j in range(1, i):
            result[i][j] = result[i-1][j-1] + result[i-1][j]
        print(result[i])

demo(10)

