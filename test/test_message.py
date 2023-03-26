#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest


class Test_Message(unittest.TestCase):


    def test_create_and_saving_and_deleting(self):
   
        

        name = "onur"
        fromUser = "fdghfhgf"

        n = 111
        e = 111


        temp_user = create_new_user(name,fromUser,n,e)

        message = {"from":"me","message":"hello"}

        number = save_new_message(message,n,e)


        #save_new_message({"from":"sender","message":"hello how are you"},n,e)

        ok = False

        temp_message_object = the_message(temp_user) 

        if number in temp_message_object:
          if temp_message_object[number] == message:
            ok = True



        key_delete(temp_user)

        message_delete(temp_user)



        self.assertEqual(ok,True,"A problem on the test_encrypt_decrypt")






import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../.."))

from messaging_app.func.create_new_rsa import create_new_rsa
from messaging_app.func.create_new_user import create_new_user
from messaging_app.lib.keys_system import the_keys, key_delete
from messaging_app.lib.messages_system import the_message, message_delete
from messaging_app.func.save_new_message import save_new_message
unittest.main(exit=False)
