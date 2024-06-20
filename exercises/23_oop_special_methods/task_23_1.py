# -*- coding: utf-8 -*-

"""
Завдання 23.1

У цьому завданні необхідно створити клас IPAddress.

При створенні екземпляра класу, як аргумент передається IP-адреса та маска,
а також має виконуватися перевірка правильності адреси та маски:
* Адреса вважається коректно заданою, якщо вона:
  * складається з 4 чисел розділених точкою
  * кожне число в діапазоні від 0 до 255
* маска вважається коректною, якщо це число в діапазоні від 8 до 32 включно

Якщо маска або адреса не пройшли перевірку, необхідно згенерувати виняток
ValueError з відповідним текстом (вивід нижче).

Також, при створенні класу, повинні бути створені два атрибути екземпляра:
ip і mask, в яких містяться адреса (рядок) та маска (число) відповідно.

Приклад створення екземпляра класу:
In [1]: ip = IPAddress('10.1.1.1/24')

Атрибути ip та mask
In [2]: ip1 = IPAddress('10.1.1.1/24')

In [3]: ip1.ip
Out[3]: '10.1.1.1'

In [4]: ip1.mask
Out[4]: 24


Перевірка правильності адреси (traceback скорочено)
In [5]: ip1 = IPAddress('10.1.1/24')
---------------------------------------------------------------------------
...
ValueError: Incorrect IPv4 address

Перевірка правильності маски (traceback скорочено)
In [6]: ip1 = IPAddress('10.1.1.1/240')
---------------------------------------------------------------------------
...
ValueError: Incorrect mask

"""
class IPAddress:
    def __init__(self, ipmask):
        self.ipmask = ipmask
        self.ip = self._div(ipmask)[0]
        self.mask = self._div(ipmask)[1]

    def _check_ip (self,ipadd):
        add = ipadd.split(".")
        if len(add) != 4:
            raise ValueError("invalid length")
        flag = 0
        for octet in add:
            # print (octet)
            if 0 <= int(octet) <=255:
                flag += 1
                #print (f"{flag} - {octet}",)
                if flag == 4:
                    return ipadd
            else:
                raise ValueError("invalid ip")
    def _check_mask (self, mask):
        if 8 <= int(mask) <=32:
            return int(mask)
        else:
            raise ValueError("invalid mask")
    def _div (self, ipmask):
        x = []
        x = ipmask.split("/")
        ip = self._check_ip(x[0])
        mask = self._check_mask(x[1])
        return ip,mask

ip1 = IPAddress("6.33.33.7/23")



print (f"address {ip1}: ip {ip1.ipmask}: ipadd {ip1.ip}: ip {ip1.mask}")
