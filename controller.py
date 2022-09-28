from unittest import result
from datetime import datetime as dt
import logger
import rational
import complex




def button_add(value_x, value_y):
    rational.init(value_x, value_y)
    result = rational.add()
    return result


def button_diff(value_x, value_y):
    rational.init(value_x, value_y)
    result = rational.diff()
    return result


def button_mult(value_x, value_y):
    rational.init(value_x, value_y)
    result = rational.mult()
    return result


def button_div(value_x, value_y):
    result = complex.div(value_x, value_y)
    return result


def button_power(value_x, value_y):
    rational.init(value_x, value_y)
    result = rational.power()
    return result


def button_sqrt(value_x):
    result = complex.sqrt(value_x)
    return result


def run(choice, value_x, value_y):
    result = 0
    text_log = f"{value_x} {choice} {value_y} = "
    comand_dict = {'+': button_add,
                   '-': button_diff,
                   '*': button_mult,
                   '/': button_div,
                   '^': button_power,
                   'sqrt': button_sqrt}
    if choice in comand_dict:
        if choice != 'sqrt':
            result = comand_dict[choice](value_x, value_y)
        else:
            result = comand_dict[choice](value_x)
            text_log = f"{choice} {value_x} = "

    logger.log(text_log, result)       
    return result


logger.logger()
