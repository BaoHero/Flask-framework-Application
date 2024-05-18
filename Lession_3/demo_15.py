from flask import Flask, render_template, request, render_template_string
from werkzeug.utils import secure_filename
app = Flask(__name__)

app.config['UPLOAD_FOLDER']	= "Lession_3/static/upload_file/"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

@app.route('/')
def index():
   return render_template('template_2.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        if f:
            path = secure_filename(f.filename)
            f.save(app.config['UPLOAD_FOLDER']+path)
            return render_template_string("""
                <html>
                <head>
                    <title>Uploaded Image</title>
                </head>
                <body>
                    <h1>Image Uploaded Successfully!</h1>
                    <p>Here is your uploaded image:</p>
                    <img src="{{url_for('static',filename=filename)}}" alt="Uploaded Image" style="max-width: 500px; max-height: 500px;">
                </body>
                </html>
                """, filename="upload_file/"+path)
        return 'No file uploaded'
if __name__ == '__main__':
   app.run(debug = True)