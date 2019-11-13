#!/usr/bin/env python
""" Running_Config_Colletor.py version 0.1 """
""" Collects several runnging configuration of several Cisco IOS devices """
""" By Israel Alves dos Santos Filho - 12/11/2019 """

from netmiko import ConnectHandler
import getpass
import time
import os

""" Getting system date """ 
day=time.strftime('%d')
month=time.strftime('%m')
year=time.strftime('%Y')
today=day+"-"+month+"-"+year

""" Device info & credentials """
username = input('Username: ')
password = getpass.getpass("Password: ")
platform = 'cisco_ios'
port = '22'

""" Loadind Device List """
with open('devices.txt') as f:
    lines = f.read().splitlines()
# print (lines)

""" Directory creation """
os.mkdir(today)
os.chdir(today)

""" Configuration files creation """
for devices in lines:
    try:
        ssh_connection = ConnectHandler(device_type=platform, ip=devices, username=username, password=password, port=port)
    except Exception:
        print('SSH is not enabled for ', devices)
        continue
    output = ssh_connection.send_command('terminal length 0\n', expect_string=r'#')
    output = ssh_connection.send_command('show run\n', expect_string=r'#')
    ssh_connection.disconnect()
    filename = ssh_connection.base_prompt +'.txt'
    file = open(filename,'w')
    file.write(output)
    time.sleep(2)
    file.close()
    print('-' * 100)
    print('The device running configuration is saved on', filename)
    print('-' * 100)