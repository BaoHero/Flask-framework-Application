from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<user>')
def hello_name(user):
   return render_template('hello.html', name = user)

if __name__ == '__main__':
   app.run(debug = True)

"""
try this:

http://127.0.0.1:5000/Hius
"""