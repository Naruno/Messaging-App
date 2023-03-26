try:
    from flask import Flask, render_template, request, redirect
except:
    import pip
    package = 'flask'
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

import os
import sys

from waitress import serve

from messaging_app.lib.keys_system import the_keys
from messaging_app.lib.messages_system import  the_message
from messaging_app.func.send import add_new_user_request, send_new_message

from messaging_app.func.encrypt import encrypt_text


from messaging_app.func.save_new_message import save_new_message


from naruno.apps.remote_app import Integration

from messaging_app.func.get import get_thread

import messaging_app

app = Flask(__name__)
from messaging_app.func.integration import the_integration

@app.route('/')
def main_page():
    return render_template('home.html')
@app.route('/user-list')
def user_list():
    users = []

    temp_keys = the_keys()

    for element in temp_keys:
        if "name" in temp_keys[element]:
            users.append(temp_keys[element])
    

    return render_template('user-list.html', users=users)

@app.route('/messages/<name>')
def messages(name):

    temp_keys = the_keys()

    for element in temp_keys:
        if "name" in temp_keys[element]:
          if temp_keys[element]["name"] == name:
            return render_template('messages.html', user_id=element)

@app.route('/get-messages/<id>')
def get_messages(id):

    temp_keys = the_keys()

    if str(id) in temp_keys:
        messages = the_message(str(id))
        return render_template('messages-col.html', user=temp_keys[str(id)], messages=messages)

@app.route("/add-new-user", methods =['POST','GET'])
def add_new_users():
    if request.method == 'POST':
 
        publickey = request.form.get('publickey').replace("\n","")
        add_new_user_request(publickey)
 
        return redirect(request.referrer)

@app.route("/new-message", methods =['POST','GET'])
def send_message():
    if request.method == 'POST':
 
        user = request.form.get('user')

        text = request.form.get('text')


        temp_keys = the_keys()[user]

        encrypted = encrypt_text(text, user)

        print("\n**** encrypted: "+ encrypted)

        pubkey = temp_keys["fromUser"]

        print("\n**** pubkey: "+ pubkey)


        send_new_message(encrypted, pubkey)

        message = {"from":"me","message":text}

        
        

        save_new_message(message,temp_keys["n"],temp_keys["e"])
 
        return redirect(request.referrer)

def start_messaging_app(port=81, integration_port=8000, password="123"):
    messaging_app.func.integration.the_integration = Integration("messaging_app", port=integration_port, password=password, sended=True)
    from threading import Thread
    t = Thread(target=get_thread)
    t.start()
    serve(app, host="0.0.0.0", port=port)


