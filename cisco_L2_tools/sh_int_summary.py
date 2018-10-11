#!/usr/bin/env python
""" sh_int_summary.py version 0.2 """
""" Retrieve version from a Cisco IOS device """
""" By Israel Alves dos Santos Filho - 10/08/2018 """

from netmiko import ConnectHandler

""" Device info & credentials """
username = input('Username: ')
password = input('Password: ')
platform = 'cisco_ios'
host = '10.0.0.1'

device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)

output = device.send_command('show int summary')

print ("\n\n")
print ("This is the list of interfaces for ", host)
print (output)
print ("\n\n")

device.disconnect()