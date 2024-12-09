def get_rows_by_number(rows, start, stop = None, copy_table=False):
    """
    Получение таблицы из одной строки или из строк из интервала по номеру строки.

    Args:
        rows(list): внутреннее представление
        start(int): левая граница интревала
        stop(int): правая граница интревала
        copy_table(bool): если False, то изменения отобразятся в исходном файле.
        В противном случае исходный файл не изменится

    Returns:
        list: внутреннее представление

    Raises:
        Exception('Ошибка, использование значения start/stop с таким'
                        ' номером невозможно')
    """
    if start < 1 or stop > len(rows):
        raise Exception('Ошибка, использование значения start/stop с таким'
                        ' номером невозможно')
    try:
        if stop is None:
            table = [rows[0]] + rows[start]
        else:
            table = [rows[0]] + rows[start: stop + 1]
    except IndexError:
        print('Нет элемента с таким номером')
        return
    if copy_table:
        return table
    else:
        rows.clear()
        for row in table:
            rows.append(row)
        return rows





