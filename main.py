from flask import Flask, render_template, url_for, request, session, redirect
from flask_cors import CORS
import pymongo
import os

app = Flask(__name__)
app.secret_key = 'verysecretkey'

connection_url = os.environ.get('MONGODB_URI')
client = pymongo.MongoClient(connection_url)

# Database
db = client.get_database('people')
# Table
users = db.user

@app.route('/')
def home():
    if 'username' in session:
        return 'Logged in as ' + session['username'] + '<br>' + "<b><a href = '/logout'>click here to log out</a></b>"
    return render_template('signin.html')

@app.route('/signin', methods=['POST'])
def signin():
    returning_user = users.find_one({'name' : request.form['username']})
    if returning_user is not None:
        return 'Logged in as ' + request.form['username'] + '<br>' + "<div><a href = '/logout'>click here to log out</a></div>"
    return render_template('signin.html', 'invalid username')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        existing_user = users.find_one({'name' : request.form['username']})
        if existing_user is None:
            users.insert({'name' : request.form['username']})
            session['username'] = request.form['username']
            return redirect(url_for('home'))

        return render_template('signup.html', 'That username already exists!')

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
