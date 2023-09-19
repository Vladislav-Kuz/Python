from data_crate import *

def enter_data():
    name = enter_first_name()
    surname = enter_sec_name()
    phone = enter_phone()
    addr = enter_address()
    with open("book.txt", 'a', encoding='utf8') as file:
        file.write(f"{name} {surname} \n{phone} \n{addr}\n\n")


def print_data():
    with open("book.txt", 'r', encoding='utf8') as file:
        print(file.read())


def search_line():
    print('Выберете вариант поиска: \n'
          '1. Имя\n'
          '2. Фамилия\n'
          '3. Телефон\n'
          '4. Адрес')
    index = int(input("Введите вариант: ")) - 1
    searched = input("Введите данные для поиска: ").title()
    with open("book.txt", 'r', encoding='utf8') as file:
        # print(file)
        # print([file.read()])    # отображает форматирование
        # # каретка переехала в конец
        # file.seek(0)  # перевод каретки в позицию 0
        # print(file.readlines()) # пустой список, разбивает на список
        # file.seek(0)  # перевод каретки в позицию 0
        # print(file.read().split('\n\n'))
        data = file.read().strip().split('\n\n')
        for item in data:
            new_item = item.replace('\n', ' ').split()
            if searched in new_item[index]:
            #     print(item)
            #     print()
                print(item, end='\n\n')