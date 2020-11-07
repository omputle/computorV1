import re
from fractions import Fraction

class Reduction:
    """
        Reduces the equation into its simplest form. It splits it into the LHS
        and RHS. Then it subtracts the RHS from both sides of the equation,
        leaving the RHS to be zero.
    """
    def __init__(self, equation):
        sides = equation.split("=")
        self.lhs = sides[0].strip()
        self.rhs = sides[1].strip()

    def find_coefficients(self):
        """
            Takes LHS & RHS and finds their coefficients. Returns them in a dictionary.
        """
        sides = {}
        left_co = self.coeff_find(self.lhs)
        right_co = self.coeff_find(self.rhs)
        left_co = self.convert_coeffs(left_co)
        right_co = self.convert_coeffs(right_co)
        sides['left'] = left_co
        sides['right'] = right_co
        return sides

    def reduced_list(self):
        """
            Subtracts the RHS from the LHS to find the reduced form of the
            equation.
        """
        sides = self.find_coefficients()
        left = sides.get('left')
        right = sides.get('right')
        dif = len(left) - len(right)
        if dif > 0:
            for i in range(dif):
                right.append(float(i - i))
        elif dif < 0:
            dif = dif * -1
            for i in range(dif):
                left.append(float(i - i))
        red_list = []
        for i in range(len(left)):
            red_list.append(round(left[i] - right[i], 2))
        return red_list

    def deg_find(self, text_to_search):
        """
            Uses Regex to find the exponents of X.
        """
        pattern = re.compile(r'[xX]\^(\d*)')
        matches = pattern.findall(text_to_search)
        return matches

    def coeff_find(self, text_to_search):
        """
            Uses Regex to find the coefficients of the polynomial.
        """
        pattern = re.compile(r'([-\s]*\d+[\.\/]*[\d+]*)\s\*\s[xX]')
        matches = pattern.findall(text_to_search)
        return matches

    def convert_to_int(self, array):
        """
            Converts list of number characters into list of integers.
        """
        int_array = []
        for item in array:
            try:
                int_array.append(int(item))
            except ValueError:
                print('Non numeric degree')
                break
        int_array.sort()
        return list(set(int_array))

    def convert_coeffs(self, coeffs):
        """
            Converts list of number character into list of floats.
        """
        coeffs_array = []
        for item in coeffs:
            num = re.sub(r'\s+', '', item)
            try:
                coeffs_array.append(float(Fraction(num)))
            except ZeroDivisionError:
                print('Oops! Zero division')
        return coeffs_array