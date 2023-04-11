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
    data = _read(csv)
    data = _sort(data)
    return _filter(data)

def _read(csv):
    data = []
    for line in csv.split('\n'):
        name, age = line.split(';')
        data.append({'name': name, 'age': int(age)})
    return data

def _sort(data):
    return sorted(data, key=lambda x: int(x[1]))

def _filter():
    result_data = []
    for person in _sort():
        if person['age'] < 10:
            continue
        else:
            result_data.append(person)
    return result_data


if __name__ == '__main__':
    print(_filter())
