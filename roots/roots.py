from math import sqrt

def check_roots(a,b,c):
    discriminant = b*b - 4*a*c
    if a == 0:
        print("Not quadratic")
    elif discriminant < 0:
        print("No roots")
    else:
        dis_sqrt = sqrt(discriminant)
        x1 = (b - dis_sqrt)/(2*a)
        x2 = (b + dis_sqrt)/(2*a)
        print("x1: ", x1)
        print("x2: ", x2)

# check_roots(1, 2, 1)