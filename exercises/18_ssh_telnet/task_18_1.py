# -*- coding: utf-8 -*-
"""
Завдання 18.1

Створити функцію send_show_command.
Функція підключається SSH (за допомогою netmiko) до ОДНОГО пристрою і виконує
вказану команду.

Параметри функції:
* device - словник із параметрами підключення до пристрою
* command – команда, яку треба виконати

Функція повертає рядок із виводом команди.

Скрипт повинен надсилати команду command на всі пристрої з файлу devices.yaml
за допомогою функції send_show_command (ця частина коду написана).

У цьому розділі тести перевіряють підключення на пристроях у файлі
devices.yaml. Якщо параметри підключення до ваших пристроїв відрізняються,
потрібно змінити параметри у файлі devices.yaml.
"""
import yaml
from netmiko import Netmiko, NetmikoAuthenticationException, ConfigInvalidException


def send_show_command(device, command):
    try:
        with Netmiko(**device) as ssh:
            ssh.enable()
            # output = ssh.send_command(command, use_textfsm=True)
            output = ssh.send_command(command)

    except NetmikoAuthenticationException:
        print(f"Problem with auth {r1['host']}")
    except ConfigInvalidException:
        print(f"Wrong config {r1['host']}")
    return output


if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        print(send_show_command(dev, command))


=====================
# -*- coding: utf-8 -*-
"""
Завдання 18.1

Створити функцію send_show_command.
Функція підключається SSH (за допомогою netmiko) до ОДНОГО пристрою і виконує
вказану команду.

Параметри функції:
* device - словник із параметрами підключення до пристрою
* command – команда, яку треба виконати

Функція повертає рядок із виводом команди.

Скрипт повинен надсилати команду command на всі пристрої з файлу devices.yaml
за допомогою функції send_show_command (ця частина коду написана).

У цьому розділі тести перевіряють підключення на пристроях у файлі
devices.yaml. Якщо параметри підключення до ваших пристроїв відрізняються,
потрібно змінити параметри у файлі devices.yaml.
"""
import yaml
import click
from netmiko import Netmiko, NetmikoAuthenticationException, ConfigInvalidException


def send_show_command(device, command):
    try:
        with Netmiko(**device) as ssh:
            ssh.enable()
            # output = ssh.send_command(command, use_textfsm=True)
            output = ssh.send_command(command)

    except NetmikoAuthenticationException:
        print(f"Problem with auth {r1['host']}")
    except ConfigInvalidException:
        print(f"Wrong config {r1['host']}")
    return output


@click.command()
@click.argument("command")
def cli(command):
    # if __name__ == "__main__":

    # command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

        with click.progressbar(devices) as devices: # вывод прогресс бара
            for dev in devices:
                print(send_show_command(dev, command))


cli()
