from messaging_app.lib.keys_system import the_keys, save_keys

import os

def encrypt_text(text_data,key):
    temp_keys = the_keys()[key]
    n = temp_keys["n"]                               #declare n
    e = temp_keys["e"]                               #declare e

    #split text to 512 char chunks
    text_data = [text_data[i:i+512] for i in range(0, len(text_data), 512)]

    total = ""
    for i in text_data:
        encrypted_mess = ""     #create 

        #turn text data to bytes
        i = bytes(i, "utf-8")

        #turn bytes to int
        i = int.from_bytes(i, byteorder='big')

        encrypted_mess = str(encryption(i,e,n))
        total += encrypted_mess+"\n"




    return(total)

#encyrption funciton. m^e % n
def encryption(m,e,n):
    x = pow(m,e,n)
    return x

 