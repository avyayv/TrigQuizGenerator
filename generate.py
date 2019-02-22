import types_of_problems
import random

problem1 = types_of_problems.TrigVariableProblem()
problem2 = types_of_problems.TrigRatioProblem()
problem3 = types_of_problems.MatrixInverseProblem()
problem4 = types_of_problems.DeterminantProblem()
problem5 = types_of_problems.VectorCrossProductProblem()
problem6 = types_of_problems.AngleBetweenTwoVectorsProblem()
problem7 = types_of_problems.VectorMagnitude()
problem8 = types_of_problems.PolarForm()

problem_set = [problem1, problem2, problem3, problem4, problem5, problem6, problem7, problem8]
problems = random.sample(problem_set, 5)
for problem in problems:
    problem.print_the_problem()
    print("\n\n")
