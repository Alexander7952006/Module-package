import csv

import pickle


def save_table(rows, name, file_type):
    """
    Сохраняет внутреннее представления таблицы в файл.

    Args:
        rows(list): внутреннее представления модуля(список списков)
        name(str): название файла, который хотите создать, или полный путь к нему
        !С обязательным указанием расширения!
        file_type(str): тип файла, который хотите создать(csv, pickle или txt)

    Returns:
        None
    Raises:
        Exception('Неправильно введен тип файла')
    """
    try:
        if file_type == 'csv':
            with open(name, 'w', newline='') as file:
                file_csv = csv.writer(file, delimiter=';')
                for row in rows:
                    file_csv.writerow([el for el in row])
        elif file_type == 'pickle':
            with open(name, 'wb') as file:
                pickle.dump(rows, file)
        elif file_type == 'txt':
            res_str = ''
            len_set = set()
            for row in rows:
                for el in row:
                    len_set.add(len(el))
            try:
                for row in rows:
                    for indx in range(len(row)):
                        while len(row[indx]) != max(len_set):
                            row[indx] += ' '
            except ValueError:
                print('Вы подали на вход пустой файл')
                return
            for row in rows:
                for el in row:
                    res_str += el + ' '
                res_str += '\n'
            with open(name, 'w') as file:
                file.writelines(res_str)
        else:
            raise Exception('Неправильно введен тип файла')
    except PermissionError:
        print('Файл открыт, его нельзя изменить')
        return
