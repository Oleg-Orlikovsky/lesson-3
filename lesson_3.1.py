def div(*args):

    try:
        arg1 = int(input("Input divided "))
        arg2 = int(input("Input divider "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Wrong divider! You can't use zero as a divider"

    return res

    '''
    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Wrong number! Divider can't be null")
    '''


print(f'result  {div()}')