import math
from math import pi, sqrt
import sys
from my_class import MyClass


def my_sqr(x: int = 0) -> int:
    """
    Calculates the square of an integer
    :param x: an integer number
    :return: square number
    """
    return x ** 2


def rad_to_degree(rad: float) -> float:
    """

    :param rad:
    :return:
    """
    return rad * (180.0 / pi)


def my_maximum(a_list):
    m = -sys.maxsize

    for a_number in a_list:
        if a_number > m:
            m = a_number

    return m


def double(x):
    return 2 * x


def double_plus_square(x):
    return sqrt(x) + double(x)


def derivative_function(f, a):
    delta = 0.000000001
    # add round(number, 3)
    return round((f(a + delta) - f(a - delta))/(2 * delta), 3)


# assert(maximum([1, 4, 7] == 7))
#
# assert(sqr(0) == 0)
# assert(sqr(3) == 9)
#
# assert(rad_to_degree(0.0) == 0.0)


if __name__ == '__main__':
    # print(maximum([1, 2, 5]))
    # assert maximum([1, 4, 7]) == 7
    #
    # a_function = maximum
    #
    # print(a_function([1, 3, 4]))

    # print(my_sqr(2))
    #
    # # 2x + x**2
    # a = lambda x: 2 * x
    # print(a(2))
    #
    # # 2X + x**x
    # another_lmbda = lambda x: a(x) + my_sqr(x)
    #
    # print(another_lmbda(2))
    #
    # max([1, 2, 8])
    #
    # print(sqrt(9))
    #
    # # x**2, derivative  is 2*x

    # another_sqr = lambda x: x ** 2

    assert my_sqr(3) == 9

    # f(x) = 2 * x
    f_2_x = lambda x: 2 * x

    assert f_2_x(2) == 4

    # derivative of x*x is 2x,

    print(f'{derivative_function(my_sqr, 10)}')
    #
    assert derivative_function(my_sqr, 10) == 20

    a_class = MyClass()




    # print(derivative_function(another_sqr, 1))


