
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

def messaging_app_main_tx(tx):

    logger = get_logger("Messaging_App")
    logger.info(
                f"A transaction sended to messaging app: {tx.__dict__}"
            )
    my_pubkey = wallet_import(-1, 3)
    

    control = False
    to_User = False

    
    if tx.toUser == my_pubkey:
        control = True
        to_User = True
    logger.debug(
                f"control: {control} | to_User: {to_User}"
            )
    if control:
     if tx.data != None:
      logger.debug(f"tx.data: {tx.data}")
      if "app" in tx.data:
       
            if "addnewusern" in tx.data["action"] and to_User:
                from messaging_app.func.create_new_user import create_new_user
                create_new_user(tx.fromUser[:15], tx.fromUser, tx.data["app_data"], 0)
            elif "addnewusere" in tx.data["action"] and to_User:
                from messaging_app.func.create_new_user import create_new_user
                create_new_user(tx.fromUser[:15], tx.fromUser, 0,tx.data["app_data"])                
            elif "newmessage" in tx.data["action"] and to_User:
                from messaging_app.func.decrypt import decrypt_text
                decrypt_text(tx.data["app_data"],tx.fromUser)
                

def get_thread():
    while True:
        new_datas = messaging_app.func.integration.the_integration.get()
        if new_datas != []:
            for data in new_datas:
                messaging_app_main_tx(Transaction(data["sequence_number"], data["signature"], data["fromUser"], data["toUser"], data["data"], data["amount"], data["transaction_fee"], data["transaction_time"]))
        time.sleep(5)


