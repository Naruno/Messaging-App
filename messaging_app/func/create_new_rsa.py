from messaging_app.func.gen_keys import gen_keys
from messaging_app.messaging_app_config import KEY_BIT


def create_new_rsa():

    p,q,n,e,d = gen_keys(KEY_BIT)
    
    from messaging_app.lib.keys_system import the_keys, save_keys
    temp_keys = the_keys()

    number = str(len(temp_keys) + 1)

    temp_keys[number] = {}

    temp_keys[number]["p"] = p
    temp_keys[number]["q"] = q
    temp_keys[number]["n"] = n
    temp_keys[number]["e"] = e
    temp_keys[number]["d"] = d




    # Public key(n + e)
    # Private key(n + d)



    save_keys(temp_keys)

    return(number)
