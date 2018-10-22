#!/usr/bin/env python
""" Simple_Running_Config_Colletor.py version 0.1 """
""" Collects the runnging configuration from one Cisco IOS devices and save on a file """
""" By Israel Alves dos Santos Filho - 10/17/2018 """

from netmiko import ConnectHandler

""" Device info & credentials """
username = input('Username: ')
password = input('Password: ')
platform = 'cisco_ios'
host = input('Endereço IP: ')
port = '22'

device = ConnectHandler(device_type=platform, ip=host, username=username, password=password, port=port)

""" Generating the currenty configuration """
output = device.send_command('terminal length 0\n')
output = device.send_command('show run\n')

""" Creating the local file to store the configuration """
filename = 'Host_'+ str(host) + '.txt'
file = open(filename,'w')
file.write (output)
file.close()

device.disconnect()
print('The running configuration is saved on ', filename)