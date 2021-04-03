#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest


class Test_rsa(unittest.TestCase):

    def test_creating_and_delete_rsa(self):
        temp_rsa = create_new_rsa(64)

        self.assertEqual(temp_rsa in the_keys(),True,"A problem on the test_creating_rsa")

        key_delete(temp_rsa)

        self.assertEqual(temp_rsa not in the_keys(),True,"A problem on the test_creating_rsa")

    def test_encrypt_decrypt(self):
        temp_rsa = create_new_rsa(64)    

        text = "hello world"

        encrypted_text = encrypt_text(text,temp_rsa)  

        ok = True if decrypt_text(encrypted_text) == text else False

        key_delete(temp_rsa)


        self.assertEqual(ok,True,"A problem on the test_encrypt_decrypt")





if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), "../../.."))
    from apps.Messaging_App.func.create_new_rsa import create_new_rsa
    from apps.Messaging_App.func.encrypt import encrypt_text
    from apps.Messaging_App.func.decrypt import decrypt_text
    from apps.Messaging_App.lib.keys_system import the_keys, key_delete
    unittest.main()
