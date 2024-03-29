#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from messaging_app.lib.keys_system import the_keys, save_keys

import math

import os

def encrypt_text(text_data,key):
    temp_keys = the_keys()[key]
    n = temp_keys["n"]                               #declare n
    e = temp_keys["e"]                               #declare e

    parts = []
    true_length = 400

    for i in range(int(math.ceil(len(text_data) / true_length))):
        parts.append(text_data[i * int(true_length):i * int(true_length) + int(true_length)])
    text_data = parts

    total = ""
    for i in text_data:
        encrypted_mess = ""     #create 

        #turn text data to bytes
        i = bytes(i, "utf-8")

        #turn bytes to int
        i = int.from_bytes(i, byteorder='big')

        encrypted_mess = str(encryption(i,e,n))
        total += encrypted_mess+"\n"




    return(total)

#encyrption funciton. m^e % n
def encryption(m,e,n):
    x = pow(m,e,n)
    return x
