from math import sqrt
import cmath

def check_roots(array):
    a = array[2]
    b = array[1]
    c = array[0]
    discriminant = b*b - 4*a*c
    if discriminant < 0:
        print("Discriminant is strictly negative, the two solutions are:")
        dis_sqrt = cmath.sqrt(discriminant)
        x1 = (-b - dis_sqrt)/(2*a)
        x2 = (-b + dis_sqrt)/(2*a)
        print(round(x1.real, 2) + round(x1.imag, 2) * 1j)
        print(round(x2.real, 2) + round(x2.imag, 2) * 1j)
    elif discriminant == 0:
        print("Discriminant is zero, the solutions is:")
        dis_sqrt = sqrt(discriminant)
        x1 = (-b - dis_sqrt)/(2*a)
        print(round(x1, 2))
    else:
        print("Discriminant is strictly positive, the two solutions are:")
        dis_sqrt = sqrt(discriminant)
        x1 = (-b - dis_sqrt)/(2*a)
        x2 = (-b + dis_sqrt)/(2*a)
        print(round(x1, 2))
        print(round(x2, 2))