import yaml
from netmiko import Netmiko


command = "sh ip int br"
with open("devices.yaml") as f:
    devices = yaml.safe_load(f)
    r1 = devices[0]

ssh = Netmiko (**r1)

print (ssh.find_prompt())
print (ssh.enable())
output = ssh.send_command("sh run")
print (output)

ssh.send_config_set (["int fa0/1", "desc TEST"])
ssh.disconnect()

#-----Correct RESULT---#

import yaml
from netmiko import Netmiko


command = "sh ip int br"
with open("devices.yaml") as f:
    devices = yaml.safe_load(f)
    r1 = devices[0]


with Netmiko (**r1) as ssh:
    ssh.enable()
    output = ssh.send_command("sh clock")

print (output)

#-----------with exception
import yaml
from netmiko import Netmiko, NetmikoAuthenticationException, ConfigInvalidException

command = "sh ip int br"
with open("devices.yaml") as f:
    devices = yaml.safe_load(f)
    r1 = devices[0]

try:
    with Netmiko(**r1) as ssh:
        ssh.enable()
        output = ssh.send_command("sh clock")
        ssh.send_config_set(["int fa 0/1", "desc TEST"], error_pattern="%")

        print(ssh.send_command("sh ip int bri", use_textfsm=True)) #вывод в виде словаря
except NetmikoAuthenticationException:
    print(f"Problem with auth {r1['host']}")
except ConfigInvalidException:
    print(f"Wrong config {r1['host']}")

