import sys
from quadratic.quadratic import check_roots
from linear.linear import check_root
from reduce_equation.reduce import Reduction

class Main:
    """
        This is the main class
    """
    def __init__(self, equation):
        self.equation = equation
    
    def solve_equation(self):
        """
            This method calls validates the input and call the appropriate
            methods to solve the equation.
        """
        sides = self.equation.split("=")
        if (len(sides) != 2):
            print("Enter valid equation")
            return
        red_obj = Reduction(self.equation)
        self.reduced_equation = red_obj.reduced_list()
        self.reduced_form()
        self.find_degree()

    def reduced_form(self):
        """
            This method is repsonsible for printing the reduced form of the
            equation.
        """
        disp = 'Reduced form: '
        count = 0
        if len(self.reduced_equation) == 0:
            return
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
        """
            This method removes the trailing zeros from the reduced array of the coefficients.
            eg. input = [1,2,3,0,0,0] -> output = [1,2,3]
        """
        check = 1
        if len(array) == 1 or len(array) == 0:
            return array
        while check:
            length = len(array)
            if not array[length - 1]:
                array = array[:-1]
            else:
                check = 0
        return array

    def find_degree(self):
        """
            This method takes the final array (after removal of trailing zeros)
            and determines the degree of the polynomial. Based on that, it then
            calls an appropriate function to colculate the solution.
        """
        final_array = self.reduce_array(self.reduced_equation)
        degree = len(final_array) - 1
        if degree >= 0:
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
            print("No solution! Not possible! {} is not equal to 0 (zero)".format(final_array[0]))
        else:
            print("Check equation")

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("No equation entered!")
    elif (len(sys.argv) > 2):
        print("Enter one equation!")
    else:
        main = Main(sys.argv[1])
        main.solve_equation()