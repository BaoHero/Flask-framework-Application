from flask import Flask ,render_template , redirect ,url_for , request , session
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

app.secret_key = 'what'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'kizunaai1'
app.config['MYSQL_DB'] = 'geeklogin'

mysql = MySQL(app)

@app.route('/' , methods=['GET' , 'POST'])
def login() :
    msg = ''
    if (request.method == 'POST' and 'username' in request.form and 'password' in request.form) :
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('Select * FROM accounts WHERE username = %s and password = %s ' , (username , password))
        account = cursor.fetchone()
        if account:
            session['logined'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            session['password'] = account['password']
            msg = 'Logging Success !'
            return render_template('index.html' , msg = msg )
        else :
            msg = 'Logging fail , wrong username or password'
    return render_template('login.html' , msg = msg)
@app.route('/logout')
def logout() :
    session.pop('logined' , None)
    session.pop('id' , None)
    session.pop('username' , None)
    session.pop('password' , None)
    return redirect(url_for('login'))

if __name__ == '__main__' :
    app.run(debug=True)


