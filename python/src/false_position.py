import math
from src.utilities.function import Function


def exercise_a() -> float:
    return Function(-1, 0, lambda param: math.exp(param) + param).false_position(-0.5722)


root, iterations = exercise_a()
print("A raiz é {} e o número de iterações é {}.".format(root, iterations))


def exercise_b() -> float:
    return Function(0, 2, lambda param: math.exp(param) - 2 * math.cos(param)).false_position(0.5362)


root, iterations = exercise_b()
print("A raiz é {} e o número de iterações é {}.".format(root, iterations))


def exercise_c() -> float:
    return Function(0, 1, lambda param: math.exp(param) * math.sin(param) - 1).false_position(0.5872)


root, iterations = exercise_c()
print("A raiz é {} e o número de iterações é {}.".format(root, iterations))
