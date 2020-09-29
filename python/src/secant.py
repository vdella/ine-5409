from src.utilities.function import Function
from decimal import Decimal

print(Decimal(Function(2, 2.26, lambda param: param**2 - 5).secant()))
