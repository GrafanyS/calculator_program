var = input('Выберите с какими числами будете работать:\n1-Рациональные\n2-Комплексные\n')

if var == '1':
    num_1 = float(input('Введите первое число: '))
    num_2 = float(input('Введите второе число: '))

if var == '2':
    num_1 = complex(input('Введите первое число: '))
    num_2 = complex(input('Введите второе число: '))

math_operation = input('Выберите математическую операцию - (+,-,*,/): ')

if math_operation == '+':
    result = plus(num_1, num_2)
elif math_operation == '-':
    result = minus(num_1, num_2)
elif math_operation == '*':
    result = proiz(num_1, num_2)
elif math_operation == '/':
    result = div(num_1, num_2)
    



    