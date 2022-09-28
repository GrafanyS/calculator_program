import logger
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



def test_division(x, y):
    '''проверка деление на 0 '''
    try:
        x/y
        logger.info(f"x/y успешный с результатом: {x/y}.")
    except ZeroDivisionError as err:
        logger.exception("Ошибка ZeroDivisionError")



