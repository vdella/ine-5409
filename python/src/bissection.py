import math
from src.utilities.function import Function


def exercise_a() -> float:
    return Function(-1, 0, lambda param: math.exp(param) + param).bisection(-0.5625, 4)


def exercise_b() -> float:
    return Function(0, 2, lambda param: math.exp(param) - 2 * math.cos(param)).bisection(0.5391, 8)


def exercise_c() -> float:
    return Function(0, 1, lambda param: math.exp(param) * math.sin(param) - 1).bisection(0.5859, 7)
