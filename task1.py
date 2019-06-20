"""
1. Каждое из слов «разработка», «сокет», «декоратор»
представить в строковом формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
и также проверить тип и содержимое переменных.
"""

development, socket, decorator = 'разработка', 'сокет', 'декоратор'

print(development, type(development))
print(socket, type(socket))
print(decorator, type(decorator))

# Результаты:
# разработка <class 'str'>
# сокет <class 'str'>
# декоратор <class 'str'>

development = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
socket = '\u0441\u043e\u043a\u0435\u0442'
decorator = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

print(development, type(development))
print(socket, type(socket))
print(decorator, type(decorator))

# Результаты:
# разработка <class 'str'>
# сокет <class 'str'>
# декоратор <class 'str'>
