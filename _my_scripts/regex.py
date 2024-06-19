import re
import rich


regex = r"(\S+) +(\S+)"
line = 'ip address 10.0.13.1 255.255.255.0'
m = re.search(regex, line)

print (m.group())
print (m.group(2))
print (m.span())

# rich.inspect(m, methods=True)

print (m.groups())

regex = r"ip address (?P<ip>\S+) +(?P<mask>\S+)"
m = re.search(regex, line)
print (m.group())

print(m.groups())

print(m.groupdict())

print (m.group("ip"))


dev = {
    "name": "alex",
    "age": 20
}

print (*dev)