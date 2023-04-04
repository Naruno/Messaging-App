#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from messaging_app.func.gen_keys import gen_keys
from lib.keys_system import the_keys, save_keys
from lib.users_system import save_user

def create_new_user(n,e):

    temp_keys = the_keys()

    number = str(len(temp_keys) + 1)
    
    temp_message = {}

    temp_message["n"] = n
    temp_message["e"] = e


    save_user(temp_message,number)

    return(number)