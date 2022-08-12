# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    """
    Получение отсортированных, отфильтрованных данных из строки csv
    """
    data = _read(csv)
    sort_data = _sort(data)
    return _filter(sort_data)


def _read(csv):
    """
    Читает из строки (файла)
    """
    return [line.split(';') for line in csv.split('\n')]


def _sort(data):
    """
    Сортирует прочитанные значения по возрасту по возрастанию
    """
    return sorted(data, key=lambda line: int(line[1]))


def _filter(data):
    """
    Фильтрует итоговый результат
    """
    return [line for line in data if int(line[1]) > 10]


if __name__ == '__main__':
    print(get_users_list())
