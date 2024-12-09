import copy


def get_rows_by_index(rows, *values, copy_table=False):
    """
    Получение новой таблицы из одной строки или из строк со значениями в первом столбце,
    совпадающими с переданными аргументами val1, … , valN.

    Args:
        rows(list): внутреннее представление
        *values(int, str, bool, float): значения, с которыми будет осуществляться проверка совпадений
        copy_table(bool): если False, то изменения отобразятся в исходном файле. В противном случае исходный файл не изменится

    Returns:
        list: внутреннее представление
    Raises:
        None
    """
    if copy_table is False:
        table = copy.deepcopy(rows)
        rows.clear()
    else:
        table = rows
    result = [table[0]]
    table = table[1:]
    vals = [val for val in values]
    for indx1, row in enumerate(table):
        for indx2, el in enumerate(table):
            try:
                table[indx1][indx2] = int(table[indx1][indx2])
            except ValueError:
                try:
                    table[indx1][indx2] = float(table[indx1][indx2])
                except ValueError:
                    pass
    for row in table:
        if row[0] in vals:
            result.append([str(el) for el in row])
    if copy_table:
        return result
    else:
        for row in result:
            rows.append(row)
        return rows


