# -*- coding: utf-8 -*-
"""
Завдання 17.1

Створити функцію write_dhcp_snooping_to_csv, яка обробляє вивід команди
show dhcp snooping binding з різних файлів та записує оброблені дані до csv
файлу.

Аргументи функції:
* filenames - список з іменами файлів з вивідм show dhcp snooping binding
* output - ім'я файлу у форматі CSV, в який буде записаний результат

Функція нічого не повертає.

Наприклад, якщо як аргумент було передано список з одним файлом
sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

У підсумковому csv файлі має бути такий вміст:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21

Перший стовпець у файлі csv ім'я комутатора треба отримати з імені файлу,
інші - з вмісту в файлах.

Перевірити роботу функції на вмісті файлів sw1_dhcp_snooping.txt,
sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.

"""
import re
import csv
from pprint import pprint
from glob import glob

files = glob("sw*")

def write_dhcp_snooping_to_csv (files, output):

    regex = r'(?P<mac>\S+) +(?P<ip>\S+) + \S+ +dhcp-snooping +(?P<vlan>\S+) +(?P<intf>\S+)'


    with open(output, "w", newline="") as f:
        wr = csv.writer(f)

        wr.writerow("switch,mac,ip,vlan,interface".split(","))
    for filename in files:
        sw = filename[:3]
        with open(filename) as f:
            all_file = f.read()
            m = re.findall(regex, all_file)

            for i in m:
                lt = list(i)
                lt.insert(0,sw)
                lt = tuple (lt)
                print (lt)
                with open(output, "a", newline="") as f:
                    wr = csv.writer(f)
                    wr.writerow(lt)



write_dhcp_snooping_to_csv(files, "result.csv")