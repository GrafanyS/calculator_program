def get_ints():
    '''
    проверка на ввод числа
    '''
    while True:
        try:
            num = int(input('value = '))
            return num
        except ValueError:
            print('Ошибка. Ожидалось вещественное число.')



# get_ints()
