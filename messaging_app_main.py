from wallet.wallet import Wallet_Import

from lib.log import get_logger

logger = get_logger("Messaging_App")

def messaging_app_main_tx(tx):
    logger.info(
                f"A transaction sended to messaging app: {tx.__dict__}"
            )
    tx_pubkey = tx.toUser
    tx_pubkey_fromUser = tx.fromUser
    my_pubkey = Wallet_Import(-1, 3)
    

    control = False
    to_User = False
    from_User = False
    tx_data_app_control = False
    tx_data_app_messagingapp_control = False
    
    
    if tx_pubkey == my_pubkey or tx_pubkey in my_pubkey or my_pubkey in tx_pubkey:
        control = True
        to_User = True
    elif tx_pubkey_fromUser == my_pubkey or tx_pubkey_fromUser in my_pubkey or my_pubkey in tx_pubkey_fromUser:
        control = True
        from_User = True

    if control:
     logger.debug(
                f"control: {control} | to_User: {to_User} | from_User: {from_User}"
            )
     if tx.data != None:
      logger.debug(f"tx.data: {tx.data}")
      if "app" in tx.data:
        tx_data_app_control = True
        if tx.data["app"] == "messagingapp":
            tx_data_app_messagingapp_control = True
            if tx.data["command"] == "addnewuser" and to_User:
                from app.Messaging_App.func.create_new_user import create_new_user
                create_new_user("unknow", tx.fromUser, tx.data["n"],tx.data["e"])
            elif tx.data["command"] == "newmessage" and to_User:
                from app.Messaging_App.func.decrypt import decrypt_text
                decrypt_text(tx.data["message"],tx_pubkey_fromUser)
                
      logger.debug(f"app: {tx_data_app_control}")
      logger.debug(f"messaging_app: {tx_data_app_messagingapp_control}")




def messaging_app_main_run(port=79):

    from app.Messaging_App.web.chat import start_messaging_app
    start_messaging_app(port=port)

