"""Fibonacci using Generators"""


def series():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    range_value = input('Enter a range')
    for i in series():
        if i <= range_value:
            print i
        else:
            break

