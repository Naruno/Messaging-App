#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest


class Test_User(unittest.TestCase):


    def test_create_and_saving_and_deleting(self):
   
        

        name = "onur"

        pubkey = "onurspubkey"

        n = 111
        e = 111


        temp_user = create_new_user(name,pubkey,n,e)

        temp_user_object = the_keys()[temp_user]

        
        ok = False
        if temp_user_object["name"] == name and temp_user_object["n"] == n and temp_user_object["e"] == e:
            ok = True


        key_delete(temp_user)



        self.assertEqual(ok,True,"A problem on the test_encrypt_decrypt")





import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../.."))
from messaging_app.func.create_new_rsa import create_new_rsa
from messaging_app.func.create_new_user import create_new_user
from messaging_app.lib.keys_system import the_keys, key_delete
unittest.main(exit=False)
