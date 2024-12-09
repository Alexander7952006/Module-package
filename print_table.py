def print_table(rows):
    """
    Aналог set_values(value, column=0) для представления таблицы с одной строкой

    Args:
        rows(list): внутреннее представления модуля(список списков)
    Returns:
        None
    Raises:
        None
    """
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
    print(res_str)
