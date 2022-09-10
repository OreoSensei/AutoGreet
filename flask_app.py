# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template, redirect, session, url_for
import time
from facebookBirthday import facebookScript
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
birthdayData = {}

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/running-script')
def running_script():
    data = facebookScript()
    session['messages'] = data[0]
    global birthdayData
    birthdayData = data[1]
    return redirect(url_for('.success', messages = data[0]))

@app.route('/success')
def success():
    global birthdayData
    messages = session['messages']
    return render_template('/success.html', messages = messages, birthday = birthdayData)
if __name__ == '__main__':
    app.run(debug=True)