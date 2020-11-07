def check_root(array):
    """
        Takes an list of coefficients in a standard linear form (ax + b = 0) 
        and tries to solve it.
    """
    a = array[1]
    b = array[0]
    x = -b/a
    print("The solution is:")
    print(x)