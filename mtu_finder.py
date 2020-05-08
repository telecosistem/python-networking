"""
Created on Fri May 08 12:16:02 2019

@author: Alfredo B.
"""

import re
from my_devices_cisco import csrv1_lab, csrv2_lab
from netmiko import ConnectHandler

pattern = 'Gi...'

mtu_pattern= '\s\sMTU\s\d\d\d\d'

device_list = [csrv1_lab, csrv2_lab]

for a_device in device_list:
    net_connect = ConnectHandler(**a_device)
        #net_connect.enable()
    output = net_connect.send_command('show interface description')
    intf_id = re.findall(pattern, output)
    # Use re.findall to return a list with all pattern found. Then we'll have a list of interfaces.
    print(intf_id)

    for interface in intf_id:

        interface_output = net_connect.send_command("show interfaces {}".format(interface))

        #int_list = interface_output.split()   #splits a string into a list.
        #ind = int_list.index('MTU')
        #print('The MTU is', int_list[ind + 1])

        mtu_list = re.findall(mtu_pattern, interface_output, re.DOTALL)
        #mtu_value = re.match(mtu_pattern, interface_output)
        #to create a LIST with all mtu values.
        print(mtu_list)







