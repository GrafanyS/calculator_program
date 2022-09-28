# импорт нужных библиотек и классов
import math
import tkinter as tk
from decimal import Decimal
from unittest import result
import logger
import controller
import sys
import test


def change_mode(mode, entries):
    if mode:
        entries[0].place_forget()
        entries[1].place_forget()
        entries[2].place(relx=0.4, rely=0.13, anchor='n')
        entries[3].place(relx=0.6, rely=0.13, anchor='n')
        entries[4].place(relx=0.5, rely=0.13, anchor='n')
        entries[5].place(relx=0.4, rely=0.37, anchor='n')
        entries[6].place(relx=0.6, rely=0.37, anchor='n')
        entries[7].place(relx=0.5, rely=0.37, anchor='n')
    else:
        for i in range(2, 8):
            entries[i].place_forget()
        entries[0].place(relx=0.5, rely=0.13, anchor='n')
        entries[1].place(relx=0.5, rely=0.37, anchor='n')


def start():
    # Создание окна с задаными размерами и названием
    mainWindow = tk.Tk()
    mainWindow.geometry('500x400')
    mainWindow.title("Калькулятор")
    mainWindow.resizable(width=False, height=False)

    mode = tk.IntVar()  # Режим комплексных чисел

    # Чекбокс для перелючения на режим компдексных чисел
    flag_label = tk.Label(mainWindow, text="Комплексные\nчисла")
    # Позиционирование текста
    flag_label.place(relx=0.17, rely=0.02, anchor='n')
    flag = tk.Checkbutton(
        variable=mode, command=lambda: change_mode(mode.get(), entries))
    flag.place(relx=0.18, rely=0.13, anchor='n')

    # Создание этикетки(текста) с позиционированием для первого числа
    top_label = tk.Label(mainWindow, text="Введите первое число")
    top_label.place(relx=0.5, rely=0.04, anchor='n')  # Позиционирование текста

    # Создание этикетки(текста) с позиционированием для второго числа
    heading_label = tk.Label(mainWindow, text="Введите второе число")
    # Позиционирование текста
    heading_label.place(relx=0.5, rely=0.28, anchor='n')

    entries = []  # Список текстовых полей
    '''РАЦИОНАЛЬНЫЕ ЧИСЛА'''
    # Создание окна для ввода значения с позиционированием для первого числа
    first_entry_rac = tk.Entry(mainWindow, width=20)
    entries.append(first_entry_rac)
    # Позиционирование окна ввода занчения
    first_entry_rac.place(relx=0.5, rely=0.13, anchor='n')

    # Создание окна для ввода значения с позиционированием для второго числа
    second_entry_rac = tk.Entry(mainWindow, width=20)
    entries.append(second_entry_rac)
    # Позиционирование окна ввода занчения
    second_entry_rac.place(relx=0.5, rely=0.37, anchor='n')
    
    '''КОМПЛЕКСНЫЕ ЧИСЛА'''
    # Создание окна для ввода значения с позиционированием для первого числа
    first_entry_re = tk.Entry(mainWindow, width=7)
    first_entry_im = tk.Entry(mainWindow, width=7)
    first_entry_lable = tk.Label(mainWindow, text="+ j*")
    entries.append(first_entry_re)
    entries.append(first_entry_im)
    entries.append(first_entry_lable)
    # Создание окна для ввода значения с позиционированием для второго числа
    second_entry_re = tk.Entry(mainWindow, width=7)
    second_entry_im = tk.Entry(mainWindow, width=7)
    second_entry_lable = tk.Label(mainWindow, text="+ j*")
    entries.append(second_entry_re)
    entries.append(second_entry_im)
    entries.append(second_entry_lable)

    # Позиционирование текста
    operation = tk.Label(mainWindow, text="Операция")
    operation.place(relx=0.5, rely=0.5, anchor='n')

    result_label = tk.Label(mainWindow, text="Ваш результат: ")
    result_label.place(relx=0.5, rely=0.75, anchor='n')

    # запуск функции  add() при нажатий кнопки
    addition_button = tk.Button(text="+",
                                command=lambda: send2('+', mode.get(), entries, result_label))
    addition_button.place(relx=0.28, rely=0.58, anchor='n')
    # запуск функции minus() при нажатий кнопки
    minus_button = tk.Button(mainWindow, text="-",
                             command=lambda: send2('-', mode.get(), entries, result_label))
    minus_button.place(relx=0.38, rely=0.58, anchor='n')
    # запуск функции multiply() при нажатий кнопки
    mul_button = tk.Button(mainWindow, text="*",
                           command=lambda: send2('*', mode.get(), entries, result_label))
    mul_button.place(relx=0.48, rely=0.58, anchor='n')
    # запуск функции divide () при нажатий кнопки
    divide_button = tk.Button(mainWindow, text="/",
                              command=lambda: send2('/', mode.get(), entries, result_label))
    divide_button.place(relx=0.58, rely=0.58, anchor='n')
    
    # запуск функции sqrt () при нажатий кнопки
    sqrt_button = tk.Button(mainWindow, text="√",
                            command=lambda: send2('sqrt', mode.get(), entries, result_label))
    sqrt_button.place(relx=0.70, rely=0.58, anchor='n')
    # запуск функции power () при нажатий кнопки
    degree_button = tk.Button(mainWindow, text='^',
                              command=lambda: send2('^', mode.get(), entries, result_label))
    degree_button.place(relx=0.82, rely=0.58, anchor='n')

    mainWindow.mainloop()
    test.test_division(second_entry_rac, first_entry_im)
    test.get_ints(second_entry_rac)


def send2(operation, mode, entries, result_label):
    if mode:
        values = []
        for i in [2, 3, 5, 6]:
            if entries[i].get() == '':
                values.append(0)
            else:
                values.append(entries[i].get())
        result = controller.run(operation,
                                complex(float(values[0]), float(values[1])),
                                complex(float(values[2]), float(values[3])))
    else:
        a = entries[0].get()
        b = entries[1].get()
        if a == '':
            a = 0
        if b == '':
            b = 0
        result = controller.run(operation, Decimal(a), Decimal(b))
        
    # вывод результата на экран
    result_label.config(text="Ваш результат: " + str(result))


    logger.logger(result)
# start()

'''
подсмотрел и переработал под себя теперь стало понятно как работать с библиотекой
tkinter, мало времени, попробую сделать кнопки ввода чисовых значений, 
чтобы не надо было проверять на ввод.

'''