"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com
и преобразовать результаты из байтовового в строковый тип на кириллице.
"""

import subprocess

yandex = ['ping', 'yandex.ru']
youtube = ['ping', 'youtube.com']

yandex_ping = subprocess.Popen(yandex, stdout=subprocess.PIPE)
youtube_ping = subprocess.Popen(youtube, stdout=subprocess.PIPE)

# for line in yandex_ping.stdout:
#     print(line.decode('utf-8'))

for line in youtube_ping.stdout:
    print(line.decode('utf-8'))

# На MacOS данные приходят в байтовом представлении на латинице уже в читабельном виде.

# Результаты:
# PING yandex.ru (5.255.255.50): 56 data bytes
# 64 bytes from 5.255.255.50: icmp_seq=0 ttl=52 time=5.970 ms
# 64 bytes from 5.255.255.50: icmp_seq=1 ttl=52 time=6.010 ms
#
# PING youtube.com (64.233.161.190): 56 data bytes
# 64 bytes from 64.233.161.190: icmp_seq=0 ttl=45 time=18.343 ms
# 64 bytes from 64.233.161.190: icmp_seq=1 ttl=45 time=18.528 ms
