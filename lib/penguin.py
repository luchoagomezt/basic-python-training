from lib.bird import Bird


class Penguin(Bird):
    def __init__(self):
        pass

    # override
    def fly(self):
        print("No can do")
        return False

    def walk(self):
        print("Walking..")
        return True
