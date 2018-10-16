#!/usr/bin/env python
""" Running_Config_Colletor.py version 0.1 """
""" Collects several runnging configuration of several Cisco IOS devices """
""" By Israel Alves dos Santos Filho - 10/16/2018 """

with open('devices.txt') as f:
    lines = f.read().splitlines()
print (lines)

for device in lines:
    filename = 'Host_ '+ str(device) + '.txt'
    file = open(filename,'w')
    config = 'The device is ' + str(device)
    file.write (config)
    file.close()

#output = device.send_command('terminal length 0\n')
#output = device.send_command('show run\n')
#print(output)
#output = device.send_command('exit\n')