import math


class Function:
    """
    In a given domain, self.start and self.end are the inferior and superior limits
    in which we want to find, at least, a solution for a given mathematical expression,
    which is represented by self.expression.
    """

    def __init__(self, start, end: float, expression):
        self.start = start
        self.end = end
        self.expression = expression  # As lambda expression.
        self.exit = 0.01  # As the criteria for stopping the iterative loops.

    @staticmethod
    def same_sign(start, end) -> bool:
        return start*end > 0

    def bisection(self, stop, iterations: int = 7) -> float:

        assert not self.same_sign(self.start, self.end)

        midway: float = stop
        iterator = 0
        while iterator < iterations or abs(midway) < self.exit:
            midway = (self.start + self.end) / 2
            if Function.same_sign(self.expression(self.start), self.expression(midway)):
                self.start = midway
            else:
                self.end = midway
            iterator = iterator + 1

        return midway


def exercise_a() -> float:
    return Function(-1, 0, lambda param: math.exp(param) + param).bisection(-0.5625, 4)


def exercise_b() -> float:
    return Function(0, 2, lambda param: math.exp(param) - 2 * math.cos(param)).bisection(0.5391, 8)


def exercise_c() -> float:
    return Function(0, 1, lambda param: math.exp(param) * math.sin(param) - 1).bisection(0.5859, 20)


print(exercise_c())
