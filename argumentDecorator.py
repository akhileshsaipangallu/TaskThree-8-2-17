"""decorator with Arguments example"""


def smart_divide(func):
    def inner(a, b):
        print("Dividing %d and %d" % (a, b))
        if b == 0:
            print("Cannot divide")
            return
        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    return a/b

if __name__ == '__main__':
    print divide(6, 2)

