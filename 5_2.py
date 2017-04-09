def demo(*para):
    mean = sum(para)/len(para)
    g = [i for i in para if i > mean]
    return (mean,)+tuple(g)

print(demo(1, 2, 3, 4))
