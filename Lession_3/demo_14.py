from flask import Flask, render_template, redirect, url_for, request, flash

app = Flask(__name__)
app.secret_key = 'hius_laptop'

@app.route('/')
def index():
    return render_template('template_1.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': 
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            flash('Login Successful!', 'success')
            """
            try this to see how flash make a queue message
            return redirect(url_for('index'))
            """
        else:
            flash('Invalid username or password', 'error')
        return redirect(url_for('index'))
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
