import os

def add_new_user(name: str, phone: str, filename: str):
    """
    Добавление нового пользователя.
    """
    with open(filename, 'a', encoding = 'UTF-8') as data:
        lines = read_all(filename)
        l = lines.count('\n')
        data.write(f"{l+1};{name};{phone}\n")
    return 'Запись добавлена'
# return res if res != '' else 'Файл пустой'


def read_all(filename: str) -> str:
    """
    Возвращает все содержимое телефонной книги.
    """
    with open(filename, 'r', encoding = 'UTF-8') as data:
        res = data.read()
    return res if res != '' else 'Файл пустой'


def search_user(data: str, filename: str) -> str:
    """
    Поиск записи по критерию data.
    """
    with open(filename, 'r', encoding = 'UTF-8') as content:
        text = content.readlines()
    res = ([item for item in text if data.lower() in item.lower()])
    return (''.join(res)).replace(';', ' ') if res else 'Вхождений не найдено'



def file_exists(file: str):
    return (file in os.listdir())


def file_copy():
    with open('phonebook_copy', 'w', encoding='UTF-8') as book_copy:
        txt_to_copy = read_all(DATA_SOURCE)
        book_copy.write(txt_to_copy)
    print('Файл скопирован')


def info_copy(filename_1):
    with open(filename_1, 'r', encoding='UTF-8') as main_file:
        lst = main_file.readlines()
    for i in lst:
        print(i)
    n = int(input('Какую запись (номер строки) хотите скопировать?\n'))
    nm = input('Имя файла, в которую хотите скопировать информацию, в формате <xxxx.txt>?')
    lst_1 = lst[n-1].split(';')
    add_new_user(name=lst_1[1], phone=lst_1[2], filename=nm)
    print('Информация скопирована')
    



INFO_STRING = """
Выберите ркжим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - копирование телефонной книги в новый файл
5 - копирование конкретной записи из одного фаила в другой
"""

DATA_SOURCE = 'phones.txt'

if not file_exists(DATA_SOURCE):
    open(DATA_SOURCE, 'w', encoding = 'UTF-8')

while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(DATA_SOURCE))
        exit()
    elif mode == 2:
        name = input('Введите имя: ')
        phone = input('Введите номер телефона: ')
        print(add_new_user(name, phone, DATA_SOURCE))
        exit()
    elif mode == 3:
        search = input('Введите строку для поиска: ')
        print(search_user(search, DATA_SOURCE))
        exit()
    elif mode == 4:
        file_copy()
        exit()
    elif mode == 5:
        info_copy(DATA_SOURCE)
        exit()
