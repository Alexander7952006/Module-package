def set_value(rows, value, column=0):
    """
    Aналог set_values(value, column=0) для представления таблицы с одной строкой

    Args:
        rows(list): внутреннее представление
        value(int, str, bool, float): одно значение (типизированное согласно типу столбца).
        column(int, str): либо номер столбца, либо его строковое представление

    Returns:
        list: внутреннее представление
    Raises:
        Exception('Тип введенного value не соответствует требованиям')
        Exception('столбца с таким номером не существует')
        Exception('В таблице не одна строка, ошибка')
        KeyError('Столбца с таким индексом/названием не существует')
    """
    header = rows[0]
    if type(value) != int and type(value) != float and type(value) != bool and type(value) != str:
        raise Exception('Тип введенного value не соответствует требованиям')
    dct = {}
    types_dct = {}
    if type(column) == int:
        if column < 1:
            raise Exception('столбца с таким номером не существует')
    if len(rows) != 2:
        raise Exception('В таблице не одна строка, ошибка')
    for indx, col in enumerate(rows[1]):
        if type(column) != int:
            indx = rows[0][indx]
        else:
            indx += 1
        dct[indx] = col

    for key, val in dct.items():
        el = val
        if el == 'True' or el == 'False':
            types_dct[key] = bool
        else:
            try:
                crutch = int(el)
                types_dct[key] = int
            except ValueError:
                try:
                    crutch = float(el)
                    types_dct[key] = float
                except ValueError:
                    types_dct[key] = str
    if column not in dct:
        raise KeyError('Столбца с таким индексом/названием не существует')
    typ = types_dct[column]
    value = typ(value)
    if value is True:
        value = 'True'
    elif value is False:
        value = 'False'
    dct[column] = str(value)
    res_columns = [value for value in dct.values()]
    return [header] + [res_columns]