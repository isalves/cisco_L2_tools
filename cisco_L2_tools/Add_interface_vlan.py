#!/usr/bin/env python
""" Add_interface_vlan.py version 0.3 """
""" Associate a VLAN to physical interface on Cisco IOS device """
""" By Israel Alves dos Santos Filho - 10/22/2018 """

from netmiko import ConnectHandler

""" Device info & credentials """
print ('Credentials to be used to access the device')
username = input('Username: ')
password = input('Password: ')
platform = 'cisco_ios'
host = input('IP Address: ')
print ('\n')

""" Interface info & Vlan assigment """
print ('Interface number and VLAN assigment')
interface = input('Interface: ')
vlan = input('VLAN assigment: ')
print ('\n')

""" SSH Connection to the device """
device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)

""" Assigment physical port to VLAN commands  """
command_interface = 'interface ' + interface
command_vlan = 'switchport access vlan ' + str(vlan)
commands = [command_interface, 'switchport mode access', command_vlan]

""" VLAN application & validation  """
print ('\n\n')
print('>>>>>>>>>>OUTPUT<<<<<<<<<<')
output = device.config_mode()
print(output)
output = device.send_config_set(commands)
print(output)
output = device.exit_config_mode()
print(output)
device.disconnect()
print ('\n\n')