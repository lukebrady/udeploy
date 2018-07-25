from classlist import parse_classlist
from deployment import azure
# Import Flask and template engine.
from flask import Flask, render_template, redirect, request


app = Flask(__name__)

# Temporary web object used to keep track of authentication status
# and school choice. This will determine how redirections work.
web_object = {'authenticated' : False, 'school': None}

@app.route('/')
def index():
    if web_object['school'] is None:
        return redirect('/school')
    elif web_object['authenticated'] is not True:
        return redirect('/login')
    else:
        return render_template('index.html', school = web_object['school'])

@app.route('/login')
def login():
    return render_template('login.html', school = web_object['school'])   

@app.route('/login', methods = ['POST'])
def verify():
    username = 'admin'
    password= 'test123'

    username_v = request.form['username']
    password_v = request.form['password']
    if password_v == password and username_v == username:
        web_object['authenticated'] = True
        return redirect('/')
    else:
        return redirect('/login')

@app.route('/school')
def school():
    return render_template('school.html')

@app.route('/school', methods =['POST'])
def choose():
    school = request.form['school']
    # Add the school to the web object.
    web_object['school'] = school
    # Now return the login page for that University.
    return redirect('/login')

@app.route('/deploy', methods = ['GET','POST'])
def deploy():
    class_name = request.form['classname']
    list_file = request.files['classlist']

    print(list_file)
    # Parse the class list.
    classlist = parse_classlist('./{}'.format(list_file.filename))
    azure.deploy_classlist(class_name, classlist)
    return render_template('deploy.html',classname = class_name, classlist = classlist)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)