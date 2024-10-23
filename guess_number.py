# -*- coding: utf-8 -*-
from random import randint

MIN_VALUE = 1
MAX_VALUE = 10
PC_NUMBER = randint(MIN_VALUE, MAX_VALUE)

MESSAGE_INFO = f'Введите целое число в диапазоне [{MIN_VALUE}, {MAX_VALUE}]: '
MESSAGE_ERROR = f'Вы ввели не валидные данные :('


def main() -> None: 
    '''Игра "Проверьте себя на удачу!".'''
    print('Игра началась :)')
    while True:
        my_number:str = input(MESSAGE_INFO)

        if my_number.isdigit() and MIN_VALUE <= int(my_number) <= MAX_VALUE:
            my_number = int(my_number)
            if my_number < PC_NUMBER:
                print('Ваше число меньше того, что загадано.')
            elif my_number > PC_NUMBER:
                print('Ваше число больше того, что загадано.')
            else:
                print('Отличная интуиция! Вы угадали число ;))')
                break
        else:
            print(MESSAGE_ERROR) 

if __name__ == "__main__":
    main()