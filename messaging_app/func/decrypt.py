from messaging_app.lib.keys_system import the_keys, save_keys

from messaging_app.func.save_new_message import save_new_message

from wallet.wallet import Address, wallet_import

def decrypt_text(text_data,pubkey):

    nums = []

    for line in text_data.splitlines():
        nums.append(int(line))
    l = len(nums)
    n = nums[l-2]
    e = nums[l-1]

    print("\n\n\n e: "+str(e))
    

    temp_keys = the_keys()

    print(temp_keys)
    

    d = temp_keys["1"]["d"]
    
    if not pubkey == wallet_import(-1, 3):
        for keys in temp_keys:
          if "fromUser" in temp_keys[keys]:
            key_publickey = temp_keys[keys]["fromUser"].replace("\n","").replace(" ","")
            if pubkey == key_publickey:
                i = 0
                decrypted_Mess = ""
                while i < l -2:
                    x = decrypt(nums[i], int(d), int(n))
                    y = chr(x)
                    decrypted_Mess += y
                    i+=1
                message = {"from":"user","message":decrypted_Mess}
                save_new_message(message,temp_keys[keys]["n"],temp_keys[keys]["e"])
                return decrypted_Mess


def decrypt(c,d,n):
    x = pow(c,d,n)
    return x
