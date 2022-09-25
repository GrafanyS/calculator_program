def real_operation(a: float, b: float, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        try:
            return a / b
        except ZeroDivisionError:
            print("Деление на ноль")
    elif operation == '^':
        return a**b
    else:
        return -1
            
    



# проверка
# print(real_operation(23, 2, '*'))