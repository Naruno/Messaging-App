from messaging_app.func.gen_keys import gen_keys
from lib.keys_system import the_keys, save_keys
from lib.users_system import save_user

def create_new_user(n,e):

    temp_keys = the_keys()

    number = str(len(temp_keys) + 1)
    
    temp_message = {}

    temp_message["n"] = n
    temp_message["e"] = e


    save_user(temp_message,number)

    return(number)