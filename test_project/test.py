import time

for i in range(0, 5):
    print('Alfred')
    time.sleep(1)


def reverse_string(text):
    if type(text) is str:
        result = text[::-1]
        return f'{text} will become ==> {result}'
    else:
        return 'Argument not a string!!'


def factorial(num):
    if num >= 0:
        if 0 <= num < 2:
            return 1
        elif num > 1:
            return num * factorial(num - 1)
    return 'Input must be positive integer!!'
