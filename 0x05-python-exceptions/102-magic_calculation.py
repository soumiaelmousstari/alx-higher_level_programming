#!/usr/bin/python3
def magic_calculation(a, b):
    resulta = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            resulta += a ** b / i
        except Exception:
            resulta = b + a
            break
    return (resulta)
