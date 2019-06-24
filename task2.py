"""
2. Задание на закрепление знаний по модулю json.
Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными.
Для этого:
a. Создать функцию write_order_to_json(),
в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date).
Функция должна предусматривать запись данных в виде словаря в файл orders.json.
При записи данных указать величину отступа в 4 пробельных символа;
b. Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.
"""

import json
from datetime import date


def write_order_to_json(item, quantity, price, buyer):
    with open('orders.json', encoding='utf-8') as f_read:
        data = json.load(f_read)
    with open('orders.json', 'w', encoding='utf-8') as f_write:
        order_list = data['orders']
        order_detail = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': str(date.today())
        }
        order_list.append(order_detail)
        json.dump(data, f_write, indent=4)


write_order_to_json('Toaster', '3', '1000', 'Ivan')
write_order_to_json('PC', '1', '50000', 'Alex')
write_order_to_json('Gum', '5', '24', 'Olga')
