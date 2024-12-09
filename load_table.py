import csv

import pickle


def load_table(file_type, file_name):
    """
    Создает внутреннее представление таблицы.

    Args:
        file_type(str): тип файла, который хотите загрузить(csv, pickle или txt)
        file_name(str): название файла, который хотите загрузить, или полный путь к нему !С обязательным указанием расширения!

    Returns:
        list: Внутреннее представление таблицы(список списков)
    Raises:
        Exception('Неправильно введен тип файла')
    """
    try:
        if file_type == 'csv':
            with open(file_name, newline='') as file:
                file_csv = csv.reader(file, delimiter=';')
                rows = [_ for _ in file_csv]
        elif file_type == 'pickle':
            with open(file_name, 'rb') as file:
                rows = pickle.load(file)
        else:
            raise Exception('Неправильно введен тип файла')
    except FileNotFoundError:
        print('Неправильно указан адрес файла или файл не существует')
        return
    except PermissionError:
        print('Необходимо указать путь к файлу, а не к папке')
        return
    else:
        return rows
