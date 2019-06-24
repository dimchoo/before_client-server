"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard»
из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode).
"""

development = 'разработка'
administration = 'администрирование'
protocol = 'protocol'
standard = 'standard'

encode_development = development.encode('utf-8')
encode_administration = administration.encode('utf-8')
encode_protocol = protocol.encode('utf-8')
encode_standard = standard.encode('utf-8')

print(encode_development)
print(encode_administration)
print(encode_protocol)
print(encode_standard)

# Результаты:
# b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
# b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8
# \xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'
# b'protocol'
# b'standard'

decode_development = encode_development.decode('utf-8')
decode_administration = encode_administration.decode('utf-8')
decode_protocol = encode_protocol.decode('utf-8')
decode_standard = encode_standard.decode('utf-8')

print(decode_development)
print(decode_administration)
print(decode_protocol)
print(decode_standard)

# Результаты:
# разработка
# администрирование
# protocol
# standard
