from functools import reduce


def factorial(n: int) -> int:
    result: int = 1
    for iterator in range(1, n + 1):
        result *= iterator
    return result


def exponential(x: int, sequence_size: int = 5) -> float:
    """
    Working with approximations, we have to consider that,
    with a bigger sequence of numbers, even though the result
    will be delivered more and more slowly, our result will be
    more and more accurate.

    :param x: as the power of the euler constant.
    :param sequence_size: the bigger, the better the approximation will be.
    :return: the exponential approximation of e^x.
    """
    if sequence_size < 1:
        raise ValueError("Can't have a sequence with less than 1 element. ")
    sequence = list()
    for i in range(sequence_size + 1):
        sequence.append(x**i / factorial(i))
    return reduce(lambda a, b: a + b, sequence)

