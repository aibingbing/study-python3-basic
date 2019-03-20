# from a_package import a
test_a = 1

print(test_a)

if __name__ == "__main__":
    print("main:{0}".format(test_a))
    from a_package import a
    a.print_a_a()

test_a = 2

print("{0}  end".format(test_a))


def print_test_a():
    print("test_a:{0}".format(test_a))


print_test_a()

from a_package import  a as aa
aa.print_a_a()
