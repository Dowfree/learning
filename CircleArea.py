from math import pi as PI


def CircleArea(r):
    if isinstance(r, int) or isinstance(r, float):
        return PI*r*r
    else:
        print('You must give me an integer or float as radius.')

r = int(input('Please input the radius of the circle: '))
print(CircleArea(r))
