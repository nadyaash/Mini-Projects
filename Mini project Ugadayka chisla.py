# --------------МИНИ_ПРОЕКТ Игра "Угадайка чисел" от курса "Поколение Python": курс для начинающих.--------------
# Описание проекта: программа генерирует случайное число в диапазоне от 1 до n и просит пользователя угадать это число.
# Если догадка пользователя больше случайного числа, то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'.
# Если догадка меньше случайного числа, то программа должна вывести сообщение 'Слишком мало, попробуйте еще раз'.
# Если пользователь угадывает число, то программа должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'.
# n - назначаемое игроком число, правый предел диапазона, в котором загадывается число.

# Подключение модулей random, math
from random import *
from time import sleep

# Приветствие игрока:
def welcome():
    welcome_msg = 'Добро пожаловать в числовую угадайку'
    print(welcome_msg)

# Прощание с игроком:
def goodbuy():
    goodbay_msg = 'Спасибо, что играли в числовую угадайку. Еще увидимся...'
    print(goodbay_msg)

    
# проверка на дурака.
def is_valid(s, num):
    return s.isdigit() and 1 <= int(s) <= num


# назначение правой границы диапазона
def define_limit():
    print(f'Назначьте правую границу диапазона, a компьютер загадает число от 1 до этого числа')
    sleep(0.5)
    limit = int(input("введите правую границу диапазона здесь ==>  "))
    return limit


# создание цикла с запросом на ввод варианта угадываемого числа от пользователя
def guess_number(num):
    while True:
        number_from_user = input(f'Введите число от 1 до {num} ==>  ')
        if is_valid(number_from_user, num):
            number_from_user = int(number_from_user)
            return number_from_user
        else:
            print(f'А может быть все-таки введем целое число от 1 до {num}?')
            continue


# Сравнение введенного числа с загаданным
def compare_numbers():
    limit = define_limit()
    the_number = randint(1, limit)
    count = 0
    while True:
        user_number = guess_number(limit)
        count += 1
        if user_number < the_number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif user_number > the_number:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif user_number == the_number:
            print(f'Вы угадали!Поздравляем!')
            print(f'количество Ваших попыток: {count}.')
            break


# Предложение повторной игры
def continue_game():
    question_game_again = 'Хотите сыграть еще?'
    print(question_game_again)
    answer = input('введите "+" - если желаете продолжить, "-" - если желаете завершить игру:  ')
    if answer.lower() == '+':
        return True
    elif answer == '-':
        return goodbuy()

# старт игры
def start_game():
    while True:
        compare_numbers()
        if continue_game():
            continue
        else:
            break


welcome()
start_game()
