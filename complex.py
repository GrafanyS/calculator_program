# from math import *

# def complex_operation(a, b, operation):
#     compl_a = compl(a)    # complex number A
#     compl_b = compl(b)    # complex number B
#     if operation == '+':
#         return compl_a + compl_b
#     elif operation == '-':
#         return compl_a - compl_b
#     elif operation == '*':
#         return compl_a * compl_b
#     elif operation == '/':
#         return compl_a / compl_b
#     else:
#         return -1



# # проверка
# # print(complex_operation('1+2j', '3-1j', '*'))


def Insert_Numbers():
    # Function invite user for insert two komplex numbers and operation between it
    print('Type of complex number: a + bi\n')
    user_komplex1 = input('Insert first complex number: ')
    user_komplex2 = input('Insert second complex number: ')
    operation = input(
        'What do you want to do with that? (+, -, *, / are available only)')
    with open('results.txt', 'a') as data:
        data.write(f'({user_komplex1}){operation}({user_komplex2}) = ')
    return [user_komplex1, user_komplex2, operation]


def Take_Rational_Part(user_number):
    # Function return rational part from komplex
    rational_part = []
    for k in range(0, len(user_number)):
        if user_number[k] != ' ':
            rational_part.append(user_number[k])
        else:
            break
    rational_part = float(''.join(rational_part))
    return rational_part


def Take_Imaginary_Part(user_number):
    # Function return imaginary part
    imaginary_part = []
    for i in range(0, len(user_number)):
        if user_number[i] == 'i':
            while user_number[i] != ' ':
                imaginary_part.insert(0, user_number[i - 1])
                i -= 1
    imaginary_part.pop(0)
    imaginary_part = float(''.join(imaginary_part))
    return imaginary_part


def Take_Symbol(user_number):
    #Function return - or + between rational and imaginary parts
    symbol = []
    for l in range(0, len(user_number)):
        if user_number[l] == '-' and l != 0 or user_number[l] == '+' and l != 0:
            symbol.append(user_number[l])
    symbol = ''.join(symbol)
    return symbol


def Addition(r1, s1, i1, r2, s2, i2):
    # Function add two komplex numbers
    result = []
    result.append(r1+r2)
    if s1 == '+' and s2 == '+':
        result.append(i1+i2)
    elif s1 == '+' and s2 == '-':
        result.append(i1-i2)
    elif s1 == '-' and s2 == '+':
        result.append(i2-i1)
    else:
        result.append(-(i1+i2))
    return result


def Deduction(r1, s1, i1, r2, s2, i2):
    # Function deduction second komplex number from first
    result = []
    result.append(r1-r2)
    if s1 == '+' and s2 == '+':
        result.append(i1-i2)
    elif s1 == '+' and s2 == '-':
        result.append(i1+i2)
    elif s1 == '-' and s2 == '+':
        result.append(-i2-i1)
    else:
        result.append(i2-i1)
    return result


def Multiply(r1, s1, i1, r2, s2, i2):
    # Function multiply two komplex numbers
    result = []
    result.append(r1*r2)
    if s1 == "+" and s2 == "+" or s1 == "-" and s2 == "-":
        result.append(-i1*i2)
    else:
        result.append(i1*i2)
    if s1 == "+":
        result.append(r2*i1)
    else:
        result.append(-r2*i1)
    if s2 == "+":
        result.append(r1*i2)
    else:
        result.append(-r1*i2)
    result[0] = result[0] + result[1]
    result[1] = result[2] + result[3]
    result.pop(3)
    result.pop(2)
    return result


def division(r1, s1, i1, r2, s2, i2):
    # Function divide two komplex numbers
    numerator = []
    denominator = []
    result = []
    numerator.append(r1*r2)
    if s1 == "+" and s2 == "+" or s1 == "-" and s2 == "-":
        numerator.append(i1*i2)
    else:
        numerator.append(-i1*i2)
    if s1 == "-":
        numerator.append(-r2*i1)
    else:
        numerator.append(r2*i1)
    if s2 == "+":
        numerator.append(-r1*i2)
    else:
        numerator.append(r1*i2)
    numerator[0] = numerator[0] + numerator[1]
    numerator[1] = numerator[2] + numerator[3]
    numerator.pop(3)
    numerator.pop(2)
    denominator.append(r2**2+i2**2)
    result.append(numerator[0]/denominator[0])
    result.append(numerator[1]/denominator[0])
    return result


def record_in_file(result):
    # Added results in file'''
    with open('results.txt', 'a') as data:
        if result[1] != 0:
            for i in range(0, 2):
                if result[i] > 0 and i == 1:
                    data.write('+ ')
                elif result[i] < 0 and i == 1:
                    result[i] = -result[i]
                    result[i] = str(result[i])
                    data.write('- ')
                    data.write(result[i])
                else:
                    result[i] = str(result[i])
                    data.write(result[i])
                if i != 1:
                    data.write(' ')
            data.write('i\n')
        else:
            result[0] = str(result[0])
            data.write(f'{result[0]}\n')


def Repeat_Or_No():
    '''Function for asking user to continue or no'''
    user_choice = 'Bad answer'
    while user_choice != 'Y' or user_choice != 'N':
        user_choice = input(
            'Do you want continue work with komplex numbers? (Y or N)')
        if user_choice == 'N':
            return False
        elif user_choice == 'Y':
            return True
        else:
            print(
                'Illegal answer! Do you want continue work with komplex numbers? Insert Y or N')
