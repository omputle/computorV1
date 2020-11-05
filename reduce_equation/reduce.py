class Reduction:
    def __init__(self, equation):
        sides = equation.split("=")
        self.lhs = sides[0].strip()
        self.rhs = sides[1].strip()
        print("LHS: ", self.lhs)
        print("RHS: ", self.rhs)
    
    def find_deg(self):
        pass

    def get_coefficients(self):
        pass

    def reduced_list(self):
        pass