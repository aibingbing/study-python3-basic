b_b = 3

print("b_b_b:{}".format(b_b))


def print_b_b():
    print("print B_b:{}".format(b_b))


class ClassB:
    B = 3

    print("Class B init")

    def __init__(self, *args, **kwargs):
        self.name = "B class"

    def print_name(self):
        print("ClassB name:{}".format(self.name))

    @classmethod
    def print_b(cls):
        print("ClassB B:{}".format(cls.B))
