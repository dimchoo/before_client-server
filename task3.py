"""
3. Задание на закрепление знаний по модулю yaml.
Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата.
Для этого:
a. Подготовить данные для записи в виде словаря,
в котором первому ключу соответствует список,
второму — целое число,
третьему — вложенный словарь,
где значение каждого ключа — это целое число с юникод-символом,
отсутствующим в кодировке ASCII (например, €);
b. Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
При этом обеспечить стилизацию файла с помощью параметра default_flow_style,
а также установить возможность работы с юникодом: allow_unicode = True;
c. Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""

import yaml

my_data = {
    'first_key': ['one', 'two', 'three', 'four'],
    'second_key': 100500,
    'third_key': {
        'first_price': '100€',
        'second_price': '200€',
        'third_price': '300€'
    }
}


def write_to_yaml(filename, data):
    with open(filename, 'w', encoding='utf-8') as f_write:
        yaml.dump(data, f_write, allow_unicode=True)
    with open(filename) as f_read:
        print(f_read.read())


write_to_yaml('file1.yaml', my_data)

"""
first_key:
- one
- two
- three
- four
second_key: 100500
third_key:
  first_price: 100€
  second_price: 200€
  third_price: 300€
"""
