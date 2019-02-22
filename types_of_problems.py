import random
from pandas import *
import numpy as np

TRIG_FUNCS = ["SIN", "COS", "TAN"]
ONE_OVER_TRIG_FUNCS = ["CSC", "SEC", "COT"]

NUMBERS = ["pi/6", "pi/3", "pi/4", "pi/2", "2pi/3", "3pi/4", "pi",
"5pi/6", "11pi/6", "4pi/3", "7pi/6", "5pi/4", "5pi/3", "7pi/4", "3pi/2"]

class TrigVariableProblem:

    def __init__(self,problem=None):
        self.problem = problem
        self.generate()

    def generate(self):
        possible_restrictions = ["x<0", "x>0", ""]
        possible_variable_values = ["2x", "x", "x/2", "x/3", "x/4", "3x", "4x"]
        first_trig = random.choice(TRIG_FUNCS)
        index_of_this_function = TRIG_FUNCS.index(first_trig)
        second_one = ONE_OVER_TRIG_FUNCS
        second_one.remove(second_one[index_of_this_function-1])
        second_trig = random.choice(second_one)
        self.problem = first_trig+'('+second_trig+random.choice(possible_variable_values)+')' + ' ' + random.choice(possible_restrictions)
        return self.problem

    def print_the_problem(self):
        self.generate()
        print("SIMPLIFY")
        print(self.problem)
# class TrigEquationProblem:

class TrigRatioProblem:

    def __init__(self,problem=None):
        self.problem = problem
        self.generate()

    def generate(self):
        all = TRIG_FUNCS+ONE_OVER_TRIG_FUNCS
        self.problem = random.choice(all)+'('+random.choice(NUMBERS)+')'
        return self.problem

    def print_the_problem(self):
        self.generate()
        print("FIND THE RATIO")
        print(self.problem)

# class MatrixSolveProblem:

class MatrixInverseProblem:

    def __init__(self,problem=None):
        self.problem = problem
        self.generate()

    def generate(self):
        matrix = []
        range_of_numbers = range(0,21)
        num1 = random.choice(range_of_numbers)
        num2 = random.choice(range_of_numbers)
        num3 = random.choice(range_of_numbers)
        num4 = random.choice(range_of_numbers)
        matrix.append([])
        matrix.append([])
        matrix[0].append(num1)
        matrix[0].append(num2)
        matrix[1].append(num3)
        matrix[1].append(num4)

        self.problem = DataFrame(matrix)
        return (self.problem)

    def print_the_problem(self):
        self.generate()
        print("FIND THE INVERSE")
        print(self.problem)

class DeterminantProblem:

    def __init__(self,problem=None):
        self.problem = problem
        self.generate()

    def generate(self):
        type = random.choice(range(3,5))

        if type == 3:
            arr = np.random.randint(10, size=(type,type))

        else:
            numbers = range(0,12)
            ha1 = np.array([random.choice(numbers), random.choice(numbers), random.choice(numbers), random.choice(numbers)])
            ha2 = np.array([random.choice(numbers), random.choice(numbers), random.choice(numbers), random.choice(numbers)])
            ha3 = np.array([random.choice(numbers), random.choice(numbers), random.choice(numbers), random.choice(numbers)])
            numbers_to_choose_from = [0,0,0,0,0,0,1,0,0,0,0,2,0,0,0,0,4,5,6,3,2]
            r1 = random.choice(numbers_to_choose_from)
            r2 = random.choice(numbers_to_choose_from)
            r3 = random.choice(numbers_to_choose_from)
            r4 = random.choice(numbers_to_choose_from)
            if r1 == 0 and r2 == 0 and r3 == 0:
                r4 = random.choice(range(1,9))
            elif r1 != 0 and r2 != 0 and r3 != 0:
                r4 = 0
            newrow = np.array([r1,r2,r3,r4])
            arr = np.stack((ha1, ha2, ha3, newrow))

        self.problem = arr
        return(arr)

    def print_the_problem(self):
        self.generate()
        print("FIND THE DETERMINANT")
        print(self.problem)

class VectorCrossProductProblem:

    def __init__(self,problem=None):
        self.problem = problem
        self.generate()

    def generate(self):
        numbers = range(1,9)
        v1 = random.choice(numbers)
        v2 = random.choice(numbers)
        v3 = random.choice(numbers)
        u1 = random.choice(numbers)
        u2 = random.choice(numbers)
        u3 = random.choice(numbers)

        self.problem =  ('<%s, %s, %s> x <%s, %s, %s>') % (v1,v2,v3,u1,u2,u3)
        return self.problem

    def print_the_problem(self):
        self.generate()
        print("FIND THE CROSS PRODUCT")
        print(self.problem)

class AngleBetweenTwoVectorsProblem:

    def __init__(self,problem=None):
        self.problem = problem
        self.generate()

    def generate(self):
        numbers = range(1,10)
        v1 = random.choice(numbers)
        v2 = random.choice(numbers)
        v3 = random.choice(numbers)
        u1 = random.choice(numbers)
        u2 = random.choice(numbers)
        u3 = random.choice(numbers)

        self.problem = ('<%s, %s, %s> and <%s, %s, %s>') % (v1,v2,v3,u1,u2,u3)
        return self.problem

    def print_the_problem(self):
        self.generate()
        print("FIND THE ANGLE BETWEEN THESE VECTORS")
        print(self.problem)

class VectorMagnitude:

    def __init__(self,problem=None):
        self.problem = problem
        self.generate()

    def generate(self):
        numbers = range(1,10)
        v1 = random.choice(numbers)
        v2 = random.choice(numbers)
        v3 = random.choice(numbers)
        self.problem = ('<%s, %s, %s>') % (v1,v2,v3)
        return self.problem

    def print_the_problem(self):
        self.generate()
        print("FIND THE MAGNITUDE")
        print(self.problem)

class PolarForm:

    def __init__(self,problem=None):
        self.problem = problem
        self.generate()

    def generate(self):
        trig_numbers = ["1","0","-1"]
        second = ["-sqrt(3)i", "+sqrt(3)i", "-sqrt(3)/3i","+sqrt(3)/3i","+i","+i","-i"]
        self.problem = (random.choice(trig_numbers)+random.choice(second))
        return self.problem

    def print_the_problem(self):
        self.generate()
        print("WRITE IN POLAR FORM")
        print(self.problem)
