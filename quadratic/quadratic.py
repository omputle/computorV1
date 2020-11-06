from math import sqrt

def check_roots(array):
    a = array[2]
    b = array[1]
    c = array[0]
    discriminant = b*b - 4*a*c
    if a == 0:
        print("Not quadratic")
    elif discriminant < 0:
        print("No roots")
    elif discriminant == 0:
        print("Discriminant is zero, the solutions is:")
        dis_sqrt = sqrt(discriminant)
        x1 = (b - dis_sqrt)/(2*a)
        print(x1)
    else:
        print("Discriminant is strictly positive, the two solutions are:")
        dis_sqrt = sqrt(discriminant)
        x1 = (-b - dis_sqrt)/(2*a)
        x2 = (-b + dis_sqrt)/(2*a)
        print(x1)
        print(x2)