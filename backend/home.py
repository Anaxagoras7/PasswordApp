from flask import Blueprint, render_template, request,redirect
from flask_login import LoginManager, login_required, current_user

from models import db, Users
from FS import *

home = Blueprint('home', __name__, template_folder='../frontend')
login_manager = LoginManager()
login_manager.init_app(home)


#HOME
@home.route('/home', methods=['GET','POST'])
@login_required
def show():
    if request.method == 'POST':
        service = request.form['service']
        password = request.form['password']
        username = current_user.username

        directory = "Files\\"
        filename = directory + username + ".txt"

        try:
            text_to_append = service+" "+password
            append_new_service(filename, text_to_append)

            return redirect('/home')
        except:
            return 'There was an issue adding your task'

    else:
        l = []
        directory = "Files\\"
        username = current_user.username
        filename = directory + username + ".txt"

        filename = open(filename,'r+')
        
        n = 0
        for line in filename:
            key, value = line.split()
            S = Service()
            S.id = n
            S.service = key
            S.password = value
            l.append(S)
            n = n+1
        tasks = l

        return render_template('home.html', tasks=tasks)

#DELETE   
@home.route('/delete/<int:id>',methods=['GET','POST'])
def delete(id):
    directory = "Files\\"
    username = current_user.username
    filename = directory + username + ".txt"

    filename = open(filename,'r+')
    a_dictionary = {}
    for line in filename:
        key, value = line.split()
        a_dictionary[key] = value
    l = list(a_dictionary.keys())
    service = l[id]

    try:
        directory = "Files\\"
        username = current_user.username
        filename = directory + username + ".txt"
        delete_service(filename, service)

        return redirect('/home')
    except:
        return 'There was a problem deleting that task'

#UPDATE
@home.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    directory = "Files\\"
    username = current_user.username
    filename = directory + username + ".txt"

    filename = open(filename,'r+')
    l = []
    n = 0
    for line in filename:
        key, value = line.split()
        S = Service()
        S.id = n
        S.service = key
        S.password = value
        l.append(S)
        n = n+1
    task = l[id]
    service = task.service

    if request.method == 'POST':
        password = request.form['password']

        try:
            directory = "Files\\"
            username = current_user.username
            filename = directory + username + ".txt"
            update_service(filename, service, password)
            
            return redirect('/home')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task = task)
