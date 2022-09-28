import cmath

def add(a, b):
    return a + b


def mult(a, b):
    return a * b


def diff(a, b):
    return a - b


def div(a, b):
    if not b:
        return 'Деление на ноль'
    return a / b


def power(a, n):
    return a ** n


def sqrt(a):
    b = cmath.sqrt(a)
    if not b.imag:
        return b.real
    return b
