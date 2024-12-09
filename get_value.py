def get_value(rows, column=0):
    """
    Аналог get_values(column=0) для представления таблицы с одной строкой

    Args:
        rows(list): внутреннее представление
        column(int, str): либо номер столбца, либо его строковое представление

    Returns:
       list: значение, которое надо было получить, типизованное согласно типу столбца
     Raises:
        Exception('Ошибка, в таблице не одна строка!')
        Exception('Столбца с таким номером не существует')
   """


    if type(column) == int and column < 1:
        raise Exception('Столбца с таким номером не существует')
    if len(rows) != 2:
        raise Exception('Ошибка, в таблице не одна строка!')
    dct = {}
    for indx, el in enumerate(rows[1]):
        if type(column) != int:
            indx = rows[0][indx]
        else:
            indx += 1
        if el == 'True':
            dct[indx] = True
        elif el == 'False':
            dct[indx] = False
        else:
            try:
                dct[indx] = int(el)
            except ValueError:
                try:
                    dct[indx] = float(el)
                except ValueError:
                    dct[indx] = el
    try:
        return dct[column]
    except KeyError:
        print('Столбца с таким индексом/названием не существует')
        return