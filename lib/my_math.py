from math import pi


class MyMath:
    """
    This is my math library
    """
    def __init__(self):
        delta = 0.000000001

    def my_sqr(self, x: int = 0) -> int:
        """
        Calculates the square of an integer
        :param x: an integer number
        :return: square number
        """
        return x ** 2

    def derivative_function(self, f, a):
        # add round(number, 3)
        return round((f(a + self.delta) - f(a - self.delta))/(2 * self.delta), 3)

    def double(self, x):
        return 2 * x

    def rad_to_degree(self, rad: float) -> float:
        """

        :param rad:
        :return:
        """
        return rad * (180.0 / pi)
