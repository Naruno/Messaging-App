from messaging_app.lib.keys_system import the_keys, save_keys

from messaging_app.func.save_new_message import save_new_message

from naruno.wallet.wallet_import import Address, wallet_import

def decrypt_text(text_data,pubkey):


    

    temp_keys = the_keys()
    

    d = temp_keys["1"]["d"]
    n = temp_keys["1"]["n"]
    
    if not pubkey == wallet_import(-1, 3):
  
        for keys in temp_keys:
          if "fromUser" in temp_keys[keys]:

            key_publickey = temp_keys[keys]["fromUser"].replace("\n","").replace(" ","")
            if pubkey == key_publickey:
                total = ""

                for i in text_data.splitlines():
                    decrypted_Mess = decrypt(int(i), int(d), int(n))
                    decrypted_Mess = decrypted_Mess.to_bytes((decrypted_Mess.bit_length() + 7) // 8, byteorder='big')
                    total += decrypted_Mess.decode("utf-8")
                
                message = {"from":"user","message":total}
                save_new_message(message,temp_keys[keys]["n"],temp_keys[keys]["e"])
                return total


def decrypt(c,d,n):
    x = pow(c,d,n)
    return x



