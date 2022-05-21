# --------------МИНИ_ПРОЕКТ "Генератор безопасных паролей" от курса "Поколение Python": курс для начинающих.--------------


# подключение модулей
import random


# Constants
DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'


# считывание пользовательских данных
list_questions = [
    'Введите количество паролей для генерации  ',
    'Введите желаемую длину пароля  ',
    'Включать ли цифры 0123456789? (y/n) ',
    'Включать ли прописные буквы? (y/n) ',
    'Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n) ',
    'Включать ли символы !#$%&*+-=?@^_ ? (y/n) ',
    'Исключать ли неоднозначные символы il1Lo0O? (y/n) '
]

# получение ответов от пользователя
def get_answers(lst):
    list_answers = []
    for q in lst:
        answer = input(q)
        if answer.lower() == 'y':
            answer = True
            list_answers.append(answer)
        elif answer.lower() == 'n':
            answer = False
            list_answers.append(answer)
        else:
            list_answers.append(answer)
        #i += 1
    return list_answers


# формирование перечня возможных символов в пароле
def create_possible_symbols(lst):
    chars = ''
    if lst[2]:
        chars += DIGITS  # Добавление цифр
    if lst[3]:
        chars += UPPERCASE_LETTERS
    if lst[4]:
        chars += LOWERCASE_LETTERS
    if lst[5]:
        chars += PUNCTUATION
    if lst[6]:
        for c in 'il1Lo0O':
            chars = chars.replace(c, '')
    return chars


# Функция генерации паролей
def generate_password(length, chars):
    passwords_list = []
    for i in range(int(list_answers[0])):
        password = random.sample(chars, length)
        password = ''.join(str(x) for x in password)
        passwords_list.append(password)
    return passwords_list


# вывод на экран сгенерированных паролей
def print_passwords(lst):
    print('Ваши пароли готовы:  ')
    print(*lst, sep='\n')


list_answers = get_answers(list_questions)
chars_user = create_possible_symbols(list_answers)
passwords = generate_password(int(list_answers[1]), chars_user)
print_passwords(passwords)
