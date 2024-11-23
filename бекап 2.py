import csv

from fnmatch import *


def load_table_csv(file_name=input('Введите адрес хранения файла: ')):
    '''Функция принимает на вход строку, которая должна быть названием файла/его адресом в директории. Возвращает кортеж из значений: представление
    таблицы в виде списка с вложенными списками(строками) и строку, которую приняла на вход'''
    try:
        with open(file_name, newline='') as file:
            file_csv = csv.reader(file, delimiter=';')
            rows = [_ for _ in file_csv]
    except FileNotFoundError:
        print('Неправильно указан адрес файла или файл не существует')
    except PermissionError:
        print('Необходимо указать путь к файлу, а не к папке')
    else:
        return rows, file_name


def save_table_csv(rows, name=input('Введите адрес директории, куда хотите сохранить файл: ')):
    '''Принимает на вход список(внутреннее представление таблицы) и строку(название файла, который создастся или адрес его хранения).
    Ничего не возвращает, но создает новый файл на основе поданного списка'''
    try:
        with open(name, 'w', newline='') as file:
            file_csv = csv.writer(file, delimiter=';')
            for row in rows:
                file_csv.writerow(row)
    except PermissionError:
        return 'Файл открыт, его нельзя изменить'


def get_rows_by_number(start, stop, copy_table=False):
    '''Принимает на вход 3 значения: start - int, stop - int, и copy_table, ничего не возвращает, но создает новый файл и изменяет старый
    через функцию save_table_csv. Сама функция получает таблицу из одной строки или из строк из интервалапо номеру строки.
    ВАЖНО! Если вы хотите получить одну строку, то задайте stop значение False. Если вы не хотите чтобы исходная таблица менялась, то задайте copy_table
    любое значение кроме False'''
    rows = load_table_csv()[0]
    file_name = load_table_csv()[1]
    if start < 1 or stop > len(rows):
        return 'Ошибка, использование значения start/stop с таким номером невозможно'
    try:
        if stop is False:
            if copy_table is False:
                save_table_csv(rows[start - 1])
                save_table_csv(rows[start - 1], file_name)
            else:
                save_table_csv(rows[start - 1])
        else:
            if copy_table is False:
                save_table_csv(rows[start: stop - 1])
                save_table_csv(rows[start: stop - 1], file_name)
            else:
                save_table_csv(rows[start: stop - 1])
    except IndexError:
        return 'Нет элемента с таким индексом'


def get_rows_by_index(*values, copy_table=False):
    rows = load_table_csv()[0]
    file_name = load_table_csv()[1]
    result = []
    vals = [val for val in values]
    for indx1, row in enumerate(rows):
        for indx2, el in enumerate(row):
            if el == 'ИСТИНА':
                rows[indx1][indx2] = True
            elif el == 'ЛОЖЬ':
                rows[indx1][indx2] = False
            elif (fnmatch(el, '*') and el.count('0') + el.count('1') + el.count('2') + el.count('3') + el.count(
                    '4') + el.count('5') + el.count('6') +
                  el.count('7') + el.count('8') + el.count('9') == len(el)):
                rows[indx1][indx2] = int(el)
            elif (fnmatch(el, '*.*') and el.count('0') + el.count('1') + el.count('2') + el.count('3') + el.count(
                    '4') + el.count('5') + el.count('6') +
                  el.count('7') + el.count('8') + el.count('9') + 1 == len(el)):
                rows[indx1][indx2] = int(el)
    iteration = 0
    try:
        for val in vals:
            if val == rows[iteration][0]:
                result.append(rows[iteration])
            iteration += 1
    except IndexError:
        return 'Задано слишком большое кол-во значений'

    if copy_table is False:
        save_table_csv(result)
        save_table_csv(result, file_name)
    else:
        save_table_csv(result)


def get_column_types(by_number=True):
    rows = load_table_csv()[0]
    dct = {}
    columns = []
    for indx in range(len(rows[0])):
        column = []
        for row in rows:
            column.append(row[indx])
        columns.append(column)
    for indx, column in enumerate(columns):
        if by_number is False:
            indx = column[0]
        if column[0] == 'ИСТИНА' or column[0] == 'ЛОЖЬ':
            dct[indx] = bool
            continue
        try:
            crutch = int(column[1])
            dct[indx] = int
        except ValueError:
            try:
                crutch = float(column[1])
                dct[indx] = float
            except ValueError:
                dct[indx] = str

    return dct


def get_values(column=0):
    if type(column) == int:
        if column < 1:
            return 'столбца с таким номером не существует'
    rows = load_table_csv()[0]
    dct = {}
    value_dct = {}
    columns = []
    for indx in range(len(rows[0])):
        col = []
        for row in rows:
            col.append(row[indx])
        columns.append(col)
    for indx, col in enumerate(columns):
        if type(column) != int:
            indx = col[0]
        else:
            indx += 1
        if col[0] == 'ИСТИНА' or col[0] == 'ЛОЖЬ':
            dct[indx] = bool
            continue
        try:
            crutch = int(col[0])  # ну тут соминительно(является ли заголовок столбца его первой строккой?)
            dct[indx] = int
        except ValueError:
            try:
                crutch = float(col[0])  # ну тут соминительно(является ли заголовок столбца его первой строккой?)
                dct[indx] = float
            except ValueError:
                dct[indx] = str
    iteration = 0
    for key, value in dct.items():
        lst = []
        for el in columns[iteration]:
            if el == 'ИСТИНА':
                lst.append(True)
            elif el == 'ЛОЖЬ':
                lst.append(False)
            elif (fnmatch(el, '*') and el.count('0') + el.count('1') + el.count('2') + el.count('3') + el.count(
                    '4') + el.count('5') + el.count('6') +
                  el.count('7') + el.count('8') + el.count('9') == len(el)):
                lst.append(int(el))
            elif (fnmatch(el, '*.*') and el.count('0') + el.count('1') + el.count('2') + el.count('3') + el.count(
                    '4') + el.count('5') + el.count('6') +
                  el.count('7') + el.count('8') + el.count('9') + 1 == len(el)):
                lst.append(float(el))
            else:
                lst.append(el)
        value_dct[key] = [value(el) for el in lst]
        iteration += 1
    try:
        return value_dct[column]
    except KeyError:
        return 'Столбца с таким индексом/названием не существует'


def set_column_types(types_dict, by_number=True):
    res_rows = []
    res_columns = []
    rows = load_table_csv()[0]
    file_name = load_table_csv()[1]
    columns = []
    for indx in range(len(rows[0])):
        column = []
        for row in rows:
            column.append(row[indx])
        columns.append(column)
    if by_number is True:
        dct = {indx: el for indx, el in enumerate(columns)}
    else:
        dct = {el[0]: el for el in columns}

    try:
        for key, value in types_dict.items():
            column = []
            for el in dct[key]:
                if el == 'ИСТИНА':
                    el = True
                elif el == 'ЛОЖЬ':
                    el = False
                elif (fnmatch(el, '*.*') and el.count('0') + el.count('1') + el.count('2') + el.count('3') + el.count(
                        '4') + el.count('5') + el.count('6') +
                      el.count('7') + el.count('8') + el.count('9') + 1 == len(el)):
                    el = float(el)
                column.append(value(el))
            res_columns.append(column)
    except KeyError:
        return 'В таблице нет столбца с таким названием/индексом'
    except ValueError:
        return 'Ошибка! Нельзя конвертировать значение в указанный тип данных'
    for indx in range(len(res_columns[0])):
        row = []
        for column in res_columns:
            if column[indx] is True:
                row.append('ИСТИНА')
            elif column[indx] is False:
                row.append('ЛОЖЬ')
            else:
                row.append(str(column[indx]))
        res_rows.append(row)
    save_table_csv(res_rows, file_name)


def get_value(column=0):
    if type(column) == int:
        if column < 1:
            return 'столбца с таким номером не существует'
    rows = load_table_csv()[0]
    if len(rows) != 1:
        return 'Ошибка, в таблице не одна строка!'
    dct = {}
    value_dct = {}
    columns = []
    for el in rows[0]:
        columns.append(el)
    for indx, col in enumerate(columns):
        if type(column) != int:
            indx = col[0]
        else:
            indx += 1
        if col[0] == 'ИСТИНА' or col[0] == 'ЛОЖЬ':
            dct[indx] = bool
            continue
        try:
            crutch = int(col[0])  # ну тут соминительно(является ли заголовок столбца его первой строккой?)
            dct[indx] = int
        except ValueError:
            try:
                crutch = float(col[0])  # ну тут соминительно(является ли заголовок столбца его первой строккой?)
                dct[indx] = float
            except ValueError:
                dct[indx] = str
    iteration = 0
    for key, value in dct.items():
        el = columns[iteration]
        if el == 'ИСТИНА':
            el = True
        elif el == 'ЛОЖЬ':
            el = False
        elif (fnmatch(el, '*') and el.count('0') + el.count('1') + el.count('2') + el.count('3') + el.count(
                '4') + el.count('5') + el.count('6') +
              el.count('7') + el.count('8') + el.count('9') == len(el)):
            el = int(el)
        elif (fnmatch(el, '*.*') and el.count('0') + el.count('1') + el.count('2') + el.count('3') + el.count(
                '4') + el.count('5') + el.count('6') +
              el.count('7') + el.count('8') + el.count('9') + 1 == len(el)):
            el = float(el)
        value_dct[key] = value(el)
        iteration += 1
    try:
        return value_dct[column]
    except KeyError:
        return 'Столбца с таким индексом/названием не существует'


def set_values(values, column=0):
    dct = {}
    types_dct = {}
    if type(column) == int:
        if column < 1:
            return 'столбца с таким номером не существует'
    rows = load_table_csv()[0]
    file_name = load_table_csv()[1]
    columns = []
    res_rows = []
    for indx in range(len(rows[0])):
        col = []
        for row in rows:
            col.append(row[indx])
        columns.append(col)
    for indx, col in enumerate(columns):
        if type(column) != int:
            indx = col[0]
        else:
            indx += 1
        dct[indx] = col
    for key, value in dct.items():
        el = value[0]
        if el == 'ИСТИНА' or el == 'ЛОЖЬ':
            types_dct[key] = bool
        elif (fnmatch(el, '*') and el.count('0') + el.count('1') + el.count('2') + el.count('3') + el.count(
                '4') + el.count('5') + el.count('6') +
              el.count('7') + el.count('8') + el.count('9') == len(el)):
            types_dct[key] = int
        elif (fnmatch(el, '*.*') and el.count('0') + el.count('1') + el.count('2') + el.count('3') + el.count(
                '4') + el.count('5') + el.count('6') +
              el.count('7') + el.count('8') + el.count('9') + 1 == len(el)):
            types_dct[key] = float
        else:
            types_dct[key] = str

    try:
        if len(dct[column]) != len(values):
            return 'Кол-во значений в задаваемом столбце не соответcтвует размеру таблицы'
    except KeyError:
        return 'Столбца с таким индексом/названием не существует'
    else:
        typ = types_dct[column]
        values = [typ(el) for el in values]
        for indx in range(len(values)):
            if values[indx] is True:
                values[indx] = 'ИСТИНА'
            elif values[indx] is False:
                values[indx] = 'ЛОЖЬ'
        dct[column] = values
    res_columns = [value for value in dct.values()]
    for indx in range(len(res_columns[0])):
        row = []
        for col in res_columns:
            row.append(str(col[indx]))
        res_rows.append(row)
    save_table_csv(res_rows, file_name)


def set_value(value, column=0):
    if type(value) != int and type(value) != float and type(value) != bool and type(value) != str:
        return 'Тип введенного value не соответствует требованиям'
    dct = {}
    types_dct = {}
    if type(column) == int:
        if column < 1:
            return 'столбца с таким номером не существует'
    rows = load_table_csv()[0]
    file_name = load_table_csv()[1]
    if len(rows) != 1:
        return 'В таблице не одна строка, ошибка'
    columns = [el for el in rows[0]]
    for indx, col in enumerate(columns):
        if type(column) != int:
            indx = col[0]
        else:
            indx += 1
        dct[indx] = col
    for key, val in dct.items():
        el = val
        if el == 'ИСТИНА' or el == 'ЛОЖЬ':
            types_dct[key] = bool
        elif (fnmatch(el, '*') and el.count('0') + el.count('1') + el.count('2') + el.count('3') + el.count(
                '4') + el.count('5') + el.count('6') +
              el.count('7') + el.count('8') + el.count('9') == len(el)):
            types_dct[key] = int
        elif (fnmatch(el, '*.*') and el.count('0') + el.count('1') + el.count('2') + el.count('3') + el.count(
                '4') + el.count('5') + el.count('6') +
              el.count('7') + el.count('8') + el.count('9') + 1 == len(el)):
            types_dct[key] = float
        else:
            types_dct[key] = str

    try:
        crutch = dct[column]
    except KeyError:
        return 'Столбца с таким индексом/названием не существует'
    typ = types_dct[column]
    value = typ(value)
    if value is True:
        value = 'ИСТИНА'
    elif value is False:
        value = 'ЛОЖЬ'
    dct[column] = value
    res_columns = [str(value) for value in dct.values()]
    save_table_csv([res_columns], file_name)


def print_table():
    res_str = ''
    rows = load_table_csv()[0]
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
        return 'Вы подали на вход пустой файл'
    for row in rows:
        for el in row:
            res_str += el + ' '
        res_str += '\n'
    print(res_str)


print(get_rows_by_index(1, 5))
