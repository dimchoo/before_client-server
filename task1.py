"""
1. Задание на закрепление знаний по модулю CSV.
Написать скрипт, осуществляющий выборку определенных данных
из файлов info_1.txt, info_2.txt, info_3.txt
и формирующий новый «отчетный» файл в формате CSV.
a.	Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными,
их открытие и считывание данных. В этой функции из считанных данных необходимо с помощью
регулярных выражений извлечь значения параметров
«Изготовитель системы»,  «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список.
Должно получиться четыре списка — например,
os_prod_list, os_name_list, os_code_list, os_type_list.
В этой же функции создать главный список для хранения данных отчета — например,
main_data — и поместить в него названия столбцов отчета в виде списка:
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка
и поместить в файл main_data (также для каждого файла);
b.	Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;
c.	Проверить работу программы через вызов функции write_to_csv().
"""

import csv
import re


def get_data(*args):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    data_list = []
    sorted_data_list = []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    pattern = r'(Изготовитель системы:.*)|(Название ОС:.*)|(Код продукта:.*)|(Тип системы:.*)'
    for file in args:
        with open(file, encoding='windows-1251') as f:
            all_data = f.read()
            find_patterns = re.findall(pattern, all_data)
            for tup in find_patterns:
                for data in tup:
                    if 'Изготовитель системы' in data:
                        data = re.sub(r' +', ' ', data)
                        os_prod_list.append(re.split(':', data)[1][1:])
                    if 'Название ОС' in data:
                        data = re.sub(r' +', ' ', data)
                        os_name_list.append(re.split(':', data)[1][1:])
                    if 'Код продукта' in data:
                        data = re.sub(r' +', ' ', data)
                        os_code_list.append(re.split(':', data)[1][1:])
                    if 'Тип системы' in data:
                        data = re.sub(r' +', ' ', data)
                        os_type_list.append(re.split(':', data)[1][1:])
    data_list.append(os_prod_list)
    data_list.append(os_name_list)
    data_list.append(os_code_list)
    data_list.append(os_type_list)
    for i in range(len(*main_data) - 1):
        sorted_data_list.append([])
        for j in range(len(*main_data)):
            sorted_data_list[i].append(data_list[j][i])
    for i in sorted_data_list:
        main_data.append(i)
    return main_data


print(get_data('info_1.txt', 'info_2.txt', 'info_3.txt'))


def write_to_csv(file_name, *args):
    data = get_data(*args)
    with open(file_name, 'w', encoding='utf-8') as f:
        f_writer = csv.writer(f)
        for row in data:
            f_writer.writerow(row)


write_to_csv('result.csv', 'info_1.txt', 'info_2.txt', 'info_3.txt')
