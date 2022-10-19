import get_data
from pathlib import Path

phonebook = get_data.data_entry()


def writing_scv(phonebook):
    file = Path("Python_seminars", "SEM_7", 'Phonebook.csv')
    with open(file, 'a', encoding='utf-8') as data:
        data.write('№,Фамилия,Имя,Номер телефона,Описание\n')
        for k, v in phonebook.items():
            data.write(
                f'{k},{v[0]},{v[1]},{v[2]},{v[3]}\n')


def writing_txt(phonebook):
    file = Path("Python_seminars", "SEM_7", 'Phonebook.txt')
    with open(file, 'a', encoding='utf-8') as data:
        for k, v in phonebook.items():
            data.write(
                f'№ {k}\nФамилия: {v[0]}\nИмя: {v[1]}\nНомер телефона: {v[2]}\nОписание: {v[3]}\n\n')


writing_txt(phonebook)
writing_scv(phonebook)
