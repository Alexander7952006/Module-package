def set_values(rows, values, column=0):
    """
    Задание списка значений values для столбца таблицы (типизированных согласно типу столбца)

    Args:
        rows(list): внутреннее представление
        values(list): список значений для столбца таблицы
        column(int, str): либо номер столбца, либо его строковое представление

    Returns:
       list: внутреннее представление
    Raises:
        Exception('Cтолбца с таким номером не существует')
    """
    header = rows[0]
    dct = {}
    types_dct = {}
    if type(column) == int:
        if column < 1:
            raise Exception('Cтолбца с таким номером не существует')
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
        dct[indx] = col[1:]

    for key, value in dct.items():
        el = value[0]
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
    try:
        if len(dct[column]) != len(values):
            print('Кол-во значений в задаваемом столбце не соответcтвует размеру таблицы')
            return
    except KeyError:
        print('Столбца с таким индексом/названием не существует')
        return
    else:
        typ = types_dct[column]
        try:
            values = [str(typ(el)) for el in values]
        except ValueError:
            print('Вы ввели данные, которые нельзя типизировать')
            return
        for indx in range(len(values)):
            if values[indx] is True:
                values[indx] = 'True'
            elif values[indx] is False:
                values[indx] = 'False'
        dct[column] = values
    res_columns = [value for value in dct.values()]
    for indx in range(len(res_columns[0])):
        row = []
        for col in res_columns:
            row.append(col[indx])
        res_rows.append(row)
    return [header] + res_rows
