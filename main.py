import sys
from roots.roots import check_roots
from root.root import check_root
from reduce_equation.reduce import Reduction

def main_function(equation):
    print(equation)
    sides = equation.split("=")
    if (len(sides) != 2):
        print("Enter valid equation")
        return
    Reduction(equation)

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("No equations!")
    elif (len(sys.argv) > 2):
        print("Enter one equation!")
    else:
        main_function(sys.argv[1])