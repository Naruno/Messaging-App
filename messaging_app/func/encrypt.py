
from messaging_app.lib.keys_system import the_keys, save_keys

import os

def encrypt_text(text_data,key):
    temp_keys = the_keys()[key]
    n = temp_keys["n"]                               #declare n
    e = temp_keys["e"]                               #declare e

    encrypted_mess = ""     #create 
    for word in text_data:
        for char in word:
            encrypted_mess += str(encryption(ord(char),e,n))+"\n"   #encrypt by char and write to file

    encrypted_mess += str(n)+"\n"                             #print n and e
    encrypted_mess += str(e)

    return(encrypted_mess)

#encyrption funciton. m^e % n
def encryption(m,e,n):
    x = pow(m,e,n)
    return x
