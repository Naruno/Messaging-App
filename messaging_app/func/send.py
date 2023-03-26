from messaging_app.lib.keys_system import the_keys



from messaging_app.func.create_new_user import create_new_user

import messaging_app
from messaging_app.func.integration import the_integration

def add_new_user_request(publickey):
    key = the_keys()["1"]

    data = {"n":key["n"], "e":key["e"]}

    messaging_app.func.integration.the_integration.send("addnewuser", data, publickey)


    create_new_user("unknow",publickey,0,0)

def send_new_message(message,publickey):
    data = {"message":message}
    messaging_app.func.integration.the_integration.send("newmessage", data, publickey)
