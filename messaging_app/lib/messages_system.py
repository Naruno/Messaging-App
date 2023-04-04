#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import json

import os


from messaging_app.messaging_app_config import MESSAGES_PATH

def save_message(new_messages,account):
    

    temp_path = (MESSAGES_PATH+str(account)+".json")

    with open(temp_path, 'w') as messages_file:
        json.dump(new_messages, messages_file)

def message_class(account):
    temp_json = {}
    save_message(temp_json,account)
    return(temp_json)




def the_message(account):
    

    temp_path = (MESSAGES_PATH+str(account)+".json")

    if not os.path.exists(temp_path):
        return message_class(account)

    with open(temp_path, 'rb') as messages_file:
        return json.load(messages_file)

def message_delete(account):
    temp_path = MESSAGES_PATH+str(account)+".json"
    if os.path.exists(temp_path):
        os.remove(temp_path)
