import re
import json

# "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
class Reduction:
    def __init__(self, equation):
        sides = equation.split("=")
        self.lhs = sides[0].strip()
        self.rhs = sides[1].strip()
    
    def find_max_deg(self):
        left_deg = self.convert_to_int(self.deg_find(self.lhs))
        right_deg = self.convert_to_int(self.deg_find(self.rhs))
        if max(left_deg) > max(right_deg):
            print('left: ', left_deg)
            return (max(left_deg))
        else:
            return (max(right_deg))

    # def create_zeros(self, num):
    #     zeros = []
    #     for i in range(num + 1):
    #         zeros.append(i - i)
    #     print(zeros)
    
    def find_coefficients(self):
        sides = {}
        left_co = self.coeff_find(self.lhs)
        right_co = self.coeff_find(self.rhs)
        left_co = self.convert_coeffs(left_co)
        right_co = self.convert_coeffs(right_co)
        sides['left'] = left_co
        sides['right'] = right_co
        return sides

    def reduced_list(self):
        sides = self.find_coefficients()
        # print(json.dumps(sides, indent=4))
        left = sides.get('left')
        right = sides.get('right')
        dif = len(left) - len(right)
        # print(dif)
        if dif > 0:
            for i in range(dif):
                right.append(float(i - i))
        elif dif < 0:
            dif = dif * -1
            for i in range(dif):
                left.append(float(i - i))
        red_list = []
        for i in range(len(left)):
            red_list.append(left[i] - right[i])
        return red_list

    def deg_find(self, text_to_search):
        pattern = re.compile(r'[xX]\^(\d*)')
        matches = pattern.findall(text_to_search)
        return matches

    # "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
    def coeff_find(self, text_to_search):
        pattern = re.compile(r'([-\s]*[\d+\.]*\d+)\s\*\s[xX]')
        matches = pattern.findall(text_to_search)
        return matches

    def convert_to_int(self, array):
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
        coeffs_array = []
        for item in coeffs:
            num = re.sub(r'\s+', '', item)
            coeffs_array.append(float(num))
        return coeffs_array