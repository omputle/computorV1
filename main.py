import sys
from roots.roots import check_roots
from root.root import check_root
from reduce_equation.reduce import Reduction

def find_degree():
    pass

def reduced_form(array):
    disp = 'Reduced form: '
    count = 0
    for item in array:
        if count != 0:
            if item < 0:
                disp = disp + ' - '
            else:
                disp = disp + ' + '
        disp = disp + str(abs(item)) + ' X^' + str(count)
        count = count + 1
    disp = disp + ' = 0'
    print(disp)

def main_function(equation):
    sides = equation.split("=")
    if (len(sides) != 2):
        print("Enter valid equation")
        return
    red_obj = Reduction(equation)
    reduced_form(red_obj.reduced_list())

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("No equations!")
    elif (len(sys.argv) > 2):
        print("Enter one equation!")
    else:
        main_function(sys.argv[1])