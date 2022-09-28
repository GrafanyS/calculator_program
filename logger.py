from datetime import datetime as dt
import logging
from time import time


def log(data, result):
    '''функция log  принимает значения и результат вычисления
    и записывает в файл .log с указанием времени'''
    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open('logger.log', 'a', encoding='utf-8') as file:
        file.writelines(f'{time} : {data} {result}\n')
        file.write('======\n')
    
def logger():
    '''функция logger использование сандартной библиотеки logging '''
    logger2 = logging.getLogger(__name__)

    logger2.setLevel(logging.INFO)

    # настройка обработчика и форматировщика для logger2
    handler2 = logging.FileHandler(f"{__name__}.log", mode='a')
    formatter2 = logging.Formatter(
        "%(name)s %(asctime)s %(levelname)s %(message)s")

    # добавление форматировщика к обработчику
    handler2.setFormatter(formatter2)
    # добавление обработчика к логгеру
    logger2.addHandler(handler2)

    logger2.debug('Это сообщение журнала.')
    logger2.info(
        f"Тестирование пользовательского регистратора для модуля {__name__}...")
    logger2.warning(f"ПРЕДУПРЕЖДЕНИЕ {__name__}...")
    logger2.error(f"ОШИБКА{__name__}...")
    logger2.critical(f"Сообщение КРИТИЧЕСКОЙ серьезности{__name__}...\n")


""" 
Две функции логирования.
"""
