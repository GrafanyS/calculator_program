def complex_operation(a, b, operation):
    compl_a = complex(a)    # complex number A
    compl_b = complex(b)    # complex number B
    if operation == '+':
        return compl_a + compl_b
    elif operation == '-':
        return compl_a - compl_b
    elif operation == '*':
        return compl_a * compl_b
    elif operation == '/':
        return compl_a / compl_b
    else:
        return -1



# проверка
# print(complex_operation('1+2j', '3-1j', '*'))