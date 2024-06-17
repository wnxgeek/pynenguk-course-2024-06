# -*- coding: utf-8 -*-
"""
Завдання 15.2

Створити функцію parse_sh_ip_int_br, яка чекає як аргумент на ім'я файлу, в
якому знаходиться вивід команди show ip int br

Функція повинна обробляти вивід команди show ip int br та повертати такі поля:
* Interface
* IP-Address
* Status
* Protocol

Інформація повинна повертатися у вигляді списку кортежів (приклад вивід):
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'administratively down', 'down'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для отримання такого результату використовуйте регулярні вирази.
Перевірити роботу функції на прикладі файлу sh_ip_int_br.txt та
sh_ip_int_br_2.txt.

Приклад виклик функції
In [12]: parse_sh_ip_int_br("sh_ip_int_br.txt")
Out[12]:
[('FastEthernet0/0', '15.0.15.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.12.1', 'up', 'up'),
 ('FastEthernet0/2', '10.0.13.1', 'up', 'up'),
 ('FastEthernet0/3', 'unassigned', 'administratively down', 'down'),
 ('Loopback0', '10.1.1.1', 'up', 'up'),
 ('Loopback100', '100.0.0.1', 'up', 'up')]

In [13]: parse_sh_ip_int_br("sh_ip_int_br_2.txt")
Out[13]:
[('FastEthernet0/0', '15.0.15.2', 'up', 'up'),
 ('FastEthernet0/1', '10.0.12.2', 'up', 'up'),
 ('FastEthernet0/2', '10.0.13.2', 'down', 'down'),
 ('FastEthernet0/3', 'unassigned', 'administratively down', 'down'),
 ('Loopback0', '10.2.2.2', 'up', 'up')]

"""
import re
from rich.traceback import install
install(show_locals=True, extra_lines=5)

def parse_sh_ip_int_br (file):
    lists = []
    regex = r"(?P<intf>\S+) +(?P<ip>\S+) +\S+ +\S+ +(?P<status>up|down|administratively down) +(?P<prot>\S+)"
    with open(file) as f:
        for line in f:
            m2 = re.search(regex, line)
            if m2:
                lists.append(m2.groups())
        return lists

    return 0


def parse_sh_ip_int_br_new (file):
    lists = []
    regex = r"(?P<intf>\S+) +(?P<ip>\S+) +\S+ +\S+ +(?P<status>up|down|administratively down) +(?P<prot>\S+)"
    with open(file) as f:
        all_file = f.read()
    m=re.finditer(regex, all_file)
    for line_match in m:
        lists.append(line_match.groups())
    return lists

    return 0

print (parse_sh_ip_int_br("sh_ip_int_br_2.txt"))
print (parse_sh_ip_int_br_new("sh_ip_int_br_2.txt"))