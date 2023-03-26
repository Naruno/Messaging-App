
#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.


from naruno.wallet.wallet_import import wallet_import, Address
from naruno.lib.log import get_logger

from naruno.transactions.transaction import Transaction

import messaging_app
import time

import json

def messaging_app_main_tx(toUser, data, fromUser):

    logger = get_logger("Messaging_App")

    my_pubkey = wallet_import(-1, 3)
    

    control = False
    to_User = False

    
    if toUser == my_pubkey:
        control = True
        to_User = True
    logger.debug(
                f"control: {control} | to_User: {to_User}"
            )
    if control:
     if data != None:
            logger.debug(f"data: {data}")
   
            if "addnewusern" in data["action"] and to_User:
                from messaging_app.func.create_new_user import create_new_user
                create_new_user(fromUser[:15], fromUser, int(data["app_data"]), 0)
            elif "addnewusere" in data["action"] and to_User:
                from messaging_app.func.create_new_user import create_new_user
                create_new_user(fromUser[:15], fromUser, 0,int(data["app_data"]))                
            elif "newmessage" in data["action"] and to_User:
                from messaging_app.func.decrypt import decrypt_text
                decrypt_text(data["app_data"],fromUser)
                

def get_thread():
    while True:
        new_datas = messaging_app.func.integration.the_integration.get()
        if new_datas != []:
            for data in new_datas:
                print(data["data"])
                print(type(data["data"]))
                messaging_app_main_tx(data["toUser"], data["data"], data["fromUser"])
        time.sleep(5)


