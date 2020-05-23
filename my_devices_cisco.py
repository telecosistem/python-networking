#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon May 07 13:33:43 2020

@author: Alfredo B.
"""
import getpass

username = input('Username: ')
pwd = getpass.win_getpass()

csrv1_lab = {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.51',
    'username': username,
    'password': pwd,
}
csrv2_lab = {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.52',
    'username': username,
    'password': pwd,
}
csrv3_lab = {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.53',
    'username': username,
    'password': pwd,
}

"""
#Old format
csrv1_lab = {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.51',
    'username': 'python',
    'password': 'python',
}

"""



