#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json

import os
from messaging_app.func.create_new_rsa import create_new_rsa

from messaging_app.messaging_app_config import KEY_PATH, KEY_BIT

def save_keys(new_keys):
    print("saving: "+str(new_keys))
    with open(KEY_PATH, 'w') as keys_file:
        json.dump(new_keys, keys_file)

def keys_class():
    temp_json = {}
    save_keys(temp_json)
    return(temp_json)




def the_keys():

    if not os.path.exists(KEY_PATH):
        keys_class()
        create_new_rsa()

    with open(KEY_PATH, 'rb') as keys_file:
        return json.load(keys_file)

def key_delete(account):
    saved_keys = the_keys()
    if account in saved_keys:
        del saved_keys[account]
        save_keys(saved_keys)
