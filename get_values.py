def get_values(rows, column=0):
    """
    Получение списка значений (типизированных согласно типу столбца).

    Args:
        rows(list): внутреннее представление
        column(int, str): либо номер столбца, либо его строковое представление

    Returns:
        list: столбец в виде списка
    Raises:
        Exception('Столбца с таким номером не существует')
    """
    if type(column) == int:
        if column < 1:
            raise Exception('Столбца с таким номером не существует')
    header = rows[0]
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
        if col[1] == 'True' or col[1] == 'False':
            dct[indx] = bool
            continue
        try:
            crutch = int(col[1])  # ну тут соминительно(является ли заголовок столбца его первой строккой?)
            dct[indx] = int
        except ValueError:
            try:
                crutch = float(col[1])  # ну тут соминительно(является ли заголовок столбца его первой строккой?)
                dct[indx] = float
            except ValueError:
                dct[indx] = str

    iteration = 0
    for key, value in dct.items():
        lst = []
        for el in columns[iteration]:
            if el == 'True':
                lst.append(True)
            elif el == 'False':
                lst.append(False)
            else:
                try:
                    lst.append(int(el))
                except ValueError:
                    try:
                        lst.append(float(el))
                    except ValueError:
                        lst.append(el)
        value_dct[key] = [value(el) for el in lst[1:]]
        iteration += 1
    try:
        return value_dct[column]
    except KeyError:
        print('Столбца с таким индексом/названием не существует')
        return