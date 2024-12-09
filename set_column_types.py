def set_column_types(rows, types_dict, by_number=True):
    """
    Задание словаря вида столбец:тип_значений. Тип значения: int, float, bool, str (по умолчанию для всех столбцов).

    Args:
        rows(list): внутреннее представление
        types_dict(dict): словарь
        by_number(bool): Если True, то ключи в словарях - индекс столбцов,
         иначе - их строковые представления

    Returns:
        list: внутреннее представление
    Raises:
        None
    """
    header = rows[0]
    res_rows = [header]
    columns = []
    for indx in range(len(rows[0])):
        column = []
        for row in rows:
            column.append(row[indx])
        columns.append(column)
    if by_number is True:
        dct = {indx: el[1:] for indx, el in enumerate(columns)}
    else:
        dct = {el[0]: el[1:] for el in columns}
    try:
        for key, value in types_dict.items():
            for indx, el in enumerate(dct[key]):
                if el == 'True':
                    dct[key][indx] = True
                elif el == 'False':
                    dct[key][indx] = False
                else:
                    try:
                        dct[key][indx] = int(dct[key][indx])
                    except ValueError:
                        try:
                            dct[key][indx] = float(dct[key][indx])
                        except ValueError:
                            pass
                dct[key][indx] = str(value(dct[key][indx]))
    except KeyError:
        print('В таблице нет столбца с таким названием/индексом')
        return
    except ValueError:
        print('Ошибка! Нельзя конвертировать значение в указанный тип данных')
        return
    for indx in range(len(columns[0]) - 1):
        row = []
        for value in dct.values():
            row.append(value[indx])
        res_rows.append(row)
    return res_rows
