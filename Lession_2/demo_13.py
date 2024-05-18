from flask import Flask, session, redirect, url_for, request
app = Flask(__name__)
# must set secret key 
app.secret_key = 'hiu_laptop'

@app.route('/')
def index():
   if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + "<b><a href = '/logout'>click here to log out</a></b>"
   return "You are not logged in <br><a href = '/login'></b>" + "click here to log in</b></a>"

@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
   return '''
   <!DOCTYPE html>
    <html>
    <head>
        <title>Login form</title>
    </head>
    <body>
        <form action = "" method = "post">
            <input type = "text" name = "username"/>
            <input type = "submit" value = "Login"/>
        </form>
    </body>
    </html>

   '''

@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('index'))

if __name__ == '__main__':
   app.run(debug = True)