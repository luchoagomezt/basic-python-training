from my_math import MyMath
from math import pi

if __name__ == '__main__':

    a_math_instance = MyMath()

    print(a_math_instance.my_sqr(3))

    assert a_math_instance.my_sqr(3) == 9

    print(a_math_instance.rad_to_degree(pi/2))

    another_math_instance = MyMath()

    assert another_math_instance == a_math_instance

