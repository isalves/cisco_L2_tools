#!/usr/bin/env python
""" Add_interface_vlan.py version 0.1 """
""" Retrieve version from a Cisco IOS device """
""" By Israel Alves dos Santos Filho - 10/08/2018 """

from netmiko import ConnectHandler

""" Device info & credentials """
print ('Credentials to be used to access the device')
username = input('Username: ')
password = input('Password: ')
platform = 'cisco_ios'
host = '10.0.0.1'

""" Interface info & Vlan assigment """
print ('Interface number and VLAN assigment')
interface = input('Interface: ')
vlan	= input('VLAN assigment: ')

device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)

""" Assigment physical port to VLAN  """

command_interface = 'interface ' + interface
command_vlan = 'switchport access vlan ' + str(vlan)
commands = [command_interface, 'switchport mode access', command_vlan]

output = device.config_mode()
print(output)
output = device.send_config_set(commands)
print(output)
output = device.exit_config_mode()
print(output)
device.disconnect()

print ('\n\n')