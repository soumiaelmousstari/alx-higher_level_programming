#!/usr/bin/python3
def safe_print_division(a, b):
    resulta = 0

    try:
        resulta = a / b
    except ZeroDivisionError:
        resulta = None
    finally:
        print('Inside result: {}'.format(resulta))
        return (resulta)
