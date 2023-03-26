from messaging_app.lib.keys_system import the_keys

from messaging_app.lib.messages_system import the_message, save_message

def save_new_message(message,n,e):

    temp_keys = the_keys()




    for temp_element in temp_keys:
        print("\n\n\n")
        print(temp_keys[temp_element]["n"] == n and temp_keys[temp_element]["e"] == e)
        if temp_keys[temp_element]["n"] == n and temp_keys[temp_element]["e"] == e and "d" not in temp_keys[temp_element]:
            
            temp_message = the_message(temp_element)
            
            number = str(len(temp_message) + 1)

            temp_message[number] = message
            
            save_message(temp_message,temp_element)
            
            return(number)


