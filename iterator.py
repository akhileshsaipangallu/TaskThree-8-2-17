"""Iterator example"""


def function(value):
    total = 0
    iter_obj = iter(value)

    while True:
        try:
            total += next(iter_obj)
        except StopIteration:
            break
    return total

if __name__ == '__main__':
    value_list = [1, 2, 3, 4, 5]
    result = function(value_list)
    print result

