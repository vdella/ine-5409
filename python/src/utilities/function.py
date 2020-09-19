from decimal import *


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
        return start * end > 0

    def bisection(self, stop, iterations: int = 7) -> float:
        """

        :param stop: value that will be compared to self.exit in order to know
        we are decreasing the possible error.
        :param iterations: other criteria that, along side with the "stop",
        will be used to define the end of the iterative loop.
        :return: a given root found inside [self.start, self.end]
        """
        assert not self.same_sign(self.start, self.end)

        midway: float = stop
        iterator = 0
        while iterator < iterations and abs(midway) >= self.exit:
            midway = (self.start + self.end) / 2
            if Function.same_sign(self.expression(self.start), self.expression(midway)):
                self.start = midway
            else:
                self.end = midway
            iterator = iterator + 1

        return Decimal(midway)
