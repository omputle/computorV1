import sys
from quadratic.quadratic import check_roots
from linear.linear import check_root
from reduce_equation.reduce import Reduction

def reduce_array(array):
    check = 1
    if len(array) == 1:
        return array
    while check:
        length = len(array)
        if not array[length - 1]:
            array = array[:-1]
        else:
            check = 0
    return array

def find_degree(array):
    final_array = reduce_array(array)
    degree = len(final_array) - 1
    print("Polynomial degree: ", degree)
    if degree > 2:
        print("The polynomial degree is stricly greater than 2, I can't solve.")
    elif degree == 2:
        check_roots(final_array)
    elif degree == 1:
        print('linear')
        check_root(array)
    elif degree == 0 and not final_array[0]:
        print("All the real numbers are solution.")
    elif degree == 0 and final_array[0]:
        print("Not possible!", final_array[0], "is not equal to 0 (zero)")


def reduced_form(array):
    disp = 'Reduced form: '
    count = 0
    for item in array:
        if count != 0:
            if item < 0:
                disp = disp + ' - '
            else:
                disp = disp + ' + '
        disp = disp + str(abs(item)) + ' * X^' + str(count)
        count = count + 1
    disp = disp + ' = 0'
    print(disp)

def main_function(equation):
    sides = equation.split("=")
    if (len(sides) != 2):
        print("Enter valid equation")
        return
    red_obj = Reduction(equation)
    red_equation = red_obj.reduced_list()
    reduced_form(red_equation)
    find_degree(red_equation)

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("No equations!")
    elif (len(sys.argv) > 2):
        print("Enter one equation!")
    else:
        main_function(sys.argv[1])