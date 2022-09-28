import math
# import test

x = 0
y = 0

# фунцкия для инициализации значении
def init(a, b):
    global x
    global y
    x = a
    y = b
    
# функция для инициализации одного значения для операций типа sqrt
def init_value(a):
    global x
    x = a

# сложение значений
def add(): return x + y  
# вычитание значений
def diff(): return x - y  
# умножение значений
def mult(): return x * y  
# деление значений
def div():                 
    try:
        return x / y
    except ZeroDivisionError:
        print("Деление на ноль") 
 # возведение в степерь значений
def power(): return x ** y 