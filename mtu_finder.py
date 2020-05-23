#!/usr/bin/env python
"""
Created on Fri May 08 12:16:02 2019

@author: Alfredo B.
"""

import re
import numpy as np
import pandas as pd

from my_devices_cisco import csrv1_lab, csrv2_lab, csrv3_lab
from netmiko import ConnectHandler

pattern = 'Gi......'
#pattern = 'Gi[1-4].[1-9][1-9][1-9][1-9]'

mtu_pattern= '\s\sMTU\s\d\d\d\d'

device_list = [csrv1_lab, csrv2_lab, csrv3_lab]
#empty list to append all mtu values
mylist_mtu=[]


for a_device in device_list:
    net_connect = ConnectHandler(**a_device)
        #net_connect.enable()
    output = net_connect.send_command('show interface description')
    intf_name = re.findall(pattern, output)
    # Use re.findall to return a list with all pattern found. Then we'll have a list of interfaces.

#FIRST we get the name of the interfaces
    for interface in intf_name:

        interface_output = net_connect.send_command("show interfaces {}".format(interface))
        #int_list = interface_output.split()   #splits a string into a list.
        #print('The MTU is', int_list[ind + 1])

        mtu_list = re.findall(mtu_pattern, interface_output, re.DOTALL)
        #How to parse a value from the list.
        mylist_mtu.append(mtu_list)

        #to create a LIST with all mtu values.
        #print("The value of MTU: {}".format(mtu_list))

    #print(mylist_mtu)

    #Use ZIP function to integrate Interface list and MTU list.
    def_list=zip(intf_name, mylist_mtu)

    # Convert to Dictionary
    dict_intf = dict(def_list)

    # Remove Whitespaces from the dictionary
    dict_intf = {x.replace(' ', ''): v
                 for x, v in dict_intf.items()}

    #print("The Dictionary is: {}".format(dict_intf))

    df=pd.DataFrame(dict_intf.items(), columns=['Interface', 'MTU'])
    print(df)

