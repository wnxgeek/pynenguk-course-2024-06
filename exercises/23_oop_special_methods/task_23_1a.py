# -*- coding: utf-8 -*-

"""
Завдання 23.1a

Копіювати та змінити клас IPAddress із завдання 23.1.

Додати два рядкові представлення для екземплярів класу IPAddress. Як мають
виглядати рядкові представлення, треба визначити з виводу нижче:

Створення екземпляра
In [5]: ip1 = IPAddress('10.1.1.1/24')

In [6]: str(ip1)
Out[6]: 'IP address 10.1.1.1/24'

In [7]: print(ip1)
IP address 10.1.1.1/24

In [8]: ip1
Out[8]: IPAddress('10.1.1.1/24')

In [9]: ip_list = []

In [10]: ip_list.append(ip1)

In [11]: ip_list
Out[11]: [IPAddress('10.1.1.1/24')]

In [12]: print(ip_list)
[IPAddress('10.1.1.1/24')]

"""
class IPAddress:
    def __init__(self, ipmask):
        self.ipmask = ipmask
        self.ip = self._div(ipmask)[0]
        self.mask = self._div(ipmask)[1]

    def __str__(self):
        return f"IPAddress: {self.ip}/{self.mask}"
    def __repr__(self):
        return f"IPAddress: {self.ip}/{self.mask}"

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



#print (f"address {ip1}: ip {ip1.ipmask}: ipadd {ip1.ip}: ip {ip1.mask}")

ip_list = []
ip_list.append(ip1)
print (ip_list)

