class MyClass:

    def __init__(self):
        a_attribute = 1
        b_attribute = True

    def a_method(self, parameter):
        pass

    def b_method(self, parameter):
        self.a_method()
        pass
