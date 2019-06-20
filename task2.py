"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе
без преобразования в последовательность кодов (не используя методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.
"""

b_class = b'class'
b_function = b'function'
b_method = b'method'

print(b_class, len(b_class), type(b_class))
print(b_function, len(b_function), type(b_function))
print(b_method, len(b_method), type(b_method))

# Результаты:
# b'class' 5 <class 'bytes'>
# b'function' 8 <class 'bytes'>
# b'method' 6 <class 'bytes'>
