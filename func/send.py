from apps.Messaging_App.lib.keys_system import the_keys
from apps.Messaging_App.func.create_new_rsa import create_new_rsa
import os
import sys

from func.send import send
from wallet.wallet import Wallet_Import

def add_new_user_request(publickey):
    key = the_keys()["1"]

    data = {"app":"messagingapp", "command":"addnewuser", "n":key["n"], "e":key["e"]}
    send(Wallet_Import(0,0), Wallet_Import(0,1), publickey, data = data, amount = 0)

def send_new_message(message,publickey):
    key = the_keys()["1"]

    data = {"app":"messagingapp", "command":"newmessage", "message":message}
    send(Wallet_Import(0,0), Wallet_Import(0,1), publickey, data = data, amount = 0)
