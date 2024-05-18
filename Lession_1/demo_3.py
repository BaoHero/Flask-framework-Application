from flask import Flask
app = Flask(__name__)
 
@app.route('/hello/<name>')
def hello_name(name):
   return 'Hi %s!' % name

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog number %d:' % postID

@app.route('/calculate/<float:number>')
def calculate(number):
   return 'Float number : %f' % number

@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python'

if __name__ == '__main__':
   app.run()

"""
try this:
http://127.0.0.1:5000/hello/Hius

http://127.0.0.1:5000/blog/18

http://127.0.0.1:5000/calculate/20.8

http://127.0.0.1:5000/flask
http://127.0.0.1:5000/flask/

http://127.0.0.1:5000/python
http://127.0.0.1:5000/python/
"""
