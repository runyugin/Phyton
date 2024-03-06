# Модуль для действий с заметками

import os
import datetime
from tabulate import tabulate


# Метод добавления новой заметки
def new_note(data_file: str, messages: tuple[str]) -> str:
    (message_1, message_2) = messages

    last_line = ""
    id_note = 1

    with open(data_file, 'r', encoding="utf-8") as f:
        for line in f:
            pass
            last_line = line

    if last_line != "":
        id_note = int(last_line.split(';')[0])+1
    note_name = input(message_1)
    note_desc = input(message_2)
    current_time = (str)(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    with open(data_file, 'a', encoding="utf-8") as working_file:

        if id_note == 1:
            working_file.write(f'{id_note}; {note_name}; {note_desc}; {current_time}; {current_time}')
        else:
            working_file.write(f'\n{id_note}; {note_name}; {note_desc}; {current_time}; {current_time}')

        print('Заметка добавлена')

    from notes import invitation
    invitation()
    

def change_note(data_file: str, messages: tuple[str]) -> str:
    (message_1, message_2, message_3) = messages

    id_note_new = int(input(message_1))
    note_name = input(message_2)
    note_desc = input(message_3)
    edit_time = (str)(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    with open(data_file, 'r', encoding="utf-8") as working_file:
        data = working_file.readlines()
    with open(data_file, 'w', encoding="utf-8") as working_file:
        for line in data:
            id_note = int(line.split(';')[0])
            create_time = (str)(line.split(';')[3])
            if id_note != id_note_new:
                working_file.write(line)
            else:
                working_file.write(f'{id_note}; {note_name}; {note_desc}; {create_time}; {edit_time}\n')

        print('Данные заменены')

    from notes import invitation
    invitation()



# Метод удаления заметки по id 
def remove_note(data_file: str, message: str) -> str:
    removing_data = (int)(input(message))

    with open(data_file, 'r', encoding="utf-8") as working_file:
        data = working_file.readlines()
    with open(data_file, 'w', encoding="utf-8") as working_file:
        for line in data:
            id_note = int(line.split(';')[0])
            if id_note != removing_data:
                working_file.write(line)

        print('Данные удалены')

    from notes import invitation
    invitation()


# Метод для поиска информации в справочнике
def search_note_data(data_file: str, message: str) -> str:
    search_by = input(message)

    with open(data_file, 'r', encoding="utf-8") as working_file:
        note_list = []
        for line in working_file:
            if search_by in line:
                line = line.split(';')
                note_list.append(line)
        result = note_list
        print(tabulate(result, headers=['id','Name', 'Desc','Data Create','Data Edit'], tablefmt='orgtbl'))

    from notes import invitation
    invitation()


# Метод для вывода построчно файла
def read_file(data_file: str, message: str) -> str:
    if os.path.exists(data_file):
        with open(data_file, 'r', encoding="utf-8") as working_file:
            note_list = []
            for line in working_file:
                line = line.split(';')
                note_list.append(line)
            result = note_list
            print(tabulate(result, headers=['id','Name', 'Desc','Data Create','Data Edit'], tablefmt='orgtbl'))
    else:
        print(message)

    from notes import invitation
    invitation()
