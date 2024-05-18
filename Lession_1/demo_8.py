from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/sign_in/<name>')
def signIN(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST'])
def login():
   if request.method == 'POST':
      user = request.form['name_txt']
      return redirect(url_for('signIN',name = user))

app.add_url_rule('/','',lambda: render_template('login.html'))
if __name__ == '__main__':
   app.run(debug = True)