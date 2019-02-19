#!/usr/bin/env python
""" Running_Config_Colletor.py version 0.2 """
""" Collects several runnging configuration of several Cisco IOS devices """
""" By Israel Alves dos Santos Filho - 02/19/2019 """

from netmiko import ConnectHandler

""" Device info & credentials """
username = input('Username: ')
password = input('Password: ')
platform = 'cisco_ios'
port = '22'

with open('devices.txt') as f:
    lines = f.read().splitlines()
print (lines)

for devices in lines:
    ssh_connection = ConnectHandler(device_type=platform, ip=devices, username=username, password=password, secret=password, port=port)
    output = ssh_connection.send_command('terminal length 0\n')
    output = ssh_connection.send_command('show run\n')
    ssh_connection.disconnect()
    filename = 'Host_'+ str(devices) + '.txt'
    file = open(filename,'w')
    file.write (output)
    file.close()