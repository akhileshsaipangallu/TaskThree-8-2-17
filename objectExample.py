"""function as objects """


def inc(num):
    return num + 1


def dec(num):
    return num - 1


def function(func_name, value):
    return func_name(value)

if __name__ == '__main__':
    input_value = input('Enter a value\n')
    input_function = input('Enter an opration(1- to decrement' +
                           ' 2- to increment)\n')
    if input_function is 2:
        print function(inc, input_value)
    elif input_function is 1:
        print function(dec, input_value)
    else:
        print('Invalid input')

