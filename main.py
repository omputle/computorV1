import sys
from quadratic.quadratic import check_roots
from linear.linear import check_root
from reduce_equation.reduce import Reduction

class Main:
    def __init__(self, equation):
        self.equation = equation
    
    def solve_equation(self):
        sides = self.equation.split("=")
        if (len(sides) != 2):
            print("Enter valid equation")
            return
        red_obj = Reduction(self.equation)
        self.reduced_equation = red_obj.reduced_list()
        self.reduced_form()
        self.find_degree()

    def reduced_form(self):
        disp = 'Reduced form: '
        count = 0
        for item in self.reduced_equation:
            if count != 0:
                if item < 0:
                    disp = disp + ' - '
                else:
                    disp = disp + ' + '
            else:
                if item < 0:
                    disp = disp + '-'
            disp = disp + str(abs(item)) + ' * X^' + str(count)
            count = count + 1
        disp = disp + ' = 0'
        print(disp)

    def reduce_array(self, array):
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

    def find_degree(self):
        final_array = self.reduce_array(self.reduced_equation)
        degree = len(final_array) - 1
        print("Polynomial degree: ", degree)
        if degree > 2:
            print("The polynomial degree is stricly greater than 2, I can't solve.")
        elif degree == 2:
            check_roots(final_array)
        elif degree == 1:
            check_root(final_array)
        elif degree == 0 and not final_array[0]:
            print("All the real numbers are solution.")
        elif degree == 0 and final_array[0]:
            print("No solution! Not possible!", final_array[0], "is not equal to 0 (zero)")




if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("No equations!")
    elif (len(sys.argv) > 2):
        print("Enter one equation!")
    else:
        main = Main(sys.argv[1])
        main.solve_equation()