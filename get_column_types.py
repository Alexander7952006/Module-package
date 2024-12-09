def get_column_types(rows, by_number=True):
    """
    Получение словаря вида столбец:тип_значений. Тип значения: int, float, bool, str (по умолчанию для всех столбцов).

    Args:
        rows(list): внутреннее представление
        by_number(bool): Если True, то ключи в словарях - индекс столбцов, иначе - их строковые представления

    Returns:
        dict: словарь вида столбец: тип_значений.
    Raises:
        None
    """
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
        if column[1] == 'True' or column[1] == 'False':
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