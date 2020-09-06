from flask import (Flask, render_template, redirect, url_for, request, make_response, session)
import sqlite3

app = Flask(__name__)

acknowledgement = None
current_user = None
user_tasks = []


@app.route('/')
def index():
    if request.method == 'POST':
        newTask = request.form.get('newtask')
        #Adding New Task to user_tasks
        with sqlite3.connect(r"database\user_tasks.db") as connection:
            try:
                cursor = connection.cursor()
                cursor.execute("INSERT INTO %s (tasks) VALUES (%s)"%(current_user, newTask))
                connection.commit()
            except:
                print('Not able to add new task')
                connection.rollback()
        #New Task Added
    
    #Retrieve tasks for Current User
    #Retrieved
    return render_template('index.html', tasks = user_tasks, curr = current_user)


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('pass')
        #Checking Database
        authentication = False
        with sqlite3.connect(r"database\users.db") as connection:
            try:
                cursor = connection.cursor()
                cursor.execute("select * from user_list") 
                all_rows = cursor.fetchall()
                for row in all_rows:
                    if username == row[0]:
                        if password == row[1]:
                            authentication = True
                        else:
                            raise Exception("Password is Incorrect")
                        break
                    else:
                        raise Exception("No such User")
            except Exception as err:
                acknowledgement = str(err)
        #Database Checked
        if authentication:
            current_user = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', acknowledge = acknowledgement)
    return render_template('login.html')


@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = resuest.form.get('username')
        password = request.form.get('pass')
        #Update Database
        with sqlite3.connect(r"databse\users.db") as connection:
            try:
                cursor = connection.cursor()
                cursor.execute("INSERT INTO user_list (username, password) VALUES (?,?)",(username, password))
                connection.commit()
            except Exception as err:
                acknowledgement = str(err)
                connection.rollback()
        #Database Updated
        return redirect(url_for('index'))
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug = True)
