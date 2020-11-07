from math import sqrt
import cmath

def check_roots(array):
    """
        Takes an list of coefficients in a standard quadratic form 
        (ax^2 + bx + c = 0) and tries to solve it. It starts by calculating the
        discriminant. If discriminant is positive, it means the solution has 
        two real roots. If it is zero, the solution has one real root. If it 
        is negative, the solution has compex root(s).
    """
    a = array[2]
    b = array[1]
    c = array[0]
    discriminant = b*b - 4*a*c
    if discriminant < 0:
        print("Discriminant is strictly negative, the two complex solutions are:")
        dis_sqrt = cmath.sqrt(discriminant)
        x1 = (-b - dis_sqrt)/(2*a)
        x2 = (-b + dis_sqrt)/(2*a)
        print(round(x1.real, 2) + round(x1.imag, 2) * 1j)
        print(round(x2.real, 2) + round(x2.imag, 2) * 1j)
    elif discriminant == 0:
        print("Discriminant is zero, the solution is:")
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