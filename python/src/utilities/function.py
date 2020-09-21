from decimal import *


class Function:
    """
    In a given domain, self.start and self.end are the inferior and superior limits
    in which we want to find, at least, a solution for a given mathematical expression,
    which is represented by self.expression.
    """

    def __init__(self, start, end: float, expression):
        self.low_end = start
        self.high_end = end
        self.expression = expression  # As lambda expression.
        self.defined_error = 1e-6  # As the criteria for stopping the iterative loops.

    def __false_position_formulae(self, a, b: float) -> float:
        return (a * self.expression(b) - b * self.expression(a)) / (self.expression(b) - self.expression(a))

    @staticmethod
    def __same_sign(start, end) -> bool:
        return start * end > 0

    def bisection(self, stop) -> float and int:
        """
        :param stop: value that will be compared to self.exit in order to know
        we are decreasing the possible error.
        :return: a given root found inside [self.start, self.end]
        """
        assert not self.__same_sign(self.low_end, self.high_end)

        midway: float = stop
        i = 0

        a = self.low_end
        b = self.high_end
        expression = self.expression

        while not abs(expression(midway)) < self.defined_error:
            midway = (a + b) / 2
            if Function.__same_sign(expression(a), self.expression(midway)):
                a = midway
            else:
                b = midway
            i = i + 1

        return Decimal(midway), i

    def false_position(self, stop) -> float and int:
        """
        :param stop: value that will be compared to self.exit in order to know
        we are decreasing the possible error.
        :return: a given root found inside [self.start, self.end]
        """
        result: float = stop
        i: int = 0

        assert not Function.__same_sign(self.expression(self.low_end), self.expression(self.high_end))

        while not abs(self.expression(result)) < self.defined_error:
            if self.expression(result) == 0:
                break
            if not Function.__same_sign(self.expression(self.high_end), self.expression(result)):
                self.high_end = result
            else:
                self.low_end = result

            result = self.__false_position_formulae(self.low_end, self.high_end)
            i = i + 1

        return Decimal(result), i
