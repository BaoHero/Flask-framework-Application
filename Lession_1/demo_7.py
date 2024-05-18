from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def result():
   dict = {'phy':100,'che':80,'math':80}
   return render_template('template_2.html', result = dict)

if __name__ == '__main__':
   app.run(debug = True)