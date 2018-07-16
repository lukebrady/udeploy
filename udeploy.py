# Import Flask and template engine.
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

web_object = {'authenticated' : False}

@app.route('/')
def index():
    if web_object['authenticated'] is not True:
        return redirect('/login')
    else:
        return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')   

@app.route('/login', methods = ['POST'])
def verify():
    password= 'test123'

    password_v = request.form['password']
    if password_v == password:
        web_object['authenticated'] = True
        return redirect('/')
    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)