from datetime import datetime as dt
import logging
from time import time

logging.basicConfig(level=logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s' )
logging.debug( 'Это сообщение журнала.' )


logging.basicConfig(level=logging.INFO, filename="result.txt",filemode="a")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")

def data_recording(value_x, value_y, value_z, rezult):
    '''
    метод принимает значения x, y, z и результат вычисления
    и записывает в файл .txt с указанием времени
    '''

    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open('result.txt', 'a', encoding='utf-8') as file:        
        file.write(time + '\n')
        file.write('\n' + f'{value_x} = value_x' + '\n')
        file.write(f'{value_y} = value_y' + '\n')
        file.write(f'"{value_z}" = value_z' + '\n')
        file.write(f'результат вычисления = {rezult}\n')
        file.write(f'==========\n')


# result = 200
# result1 = 200
# result2 = 200
# rezult = 600
# data_recording(result, result1, result2, rezult)
