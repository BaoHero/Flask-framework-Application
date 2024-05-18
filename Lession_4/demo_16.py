from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'Book(title={self.title}, author={self.author})'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'add' in request.form:
            title = request.form['title']
            author = request.form['author']
            book = Book(title=title, author=author)
            db.session.add(book)
            db.session.commit()
        elif 'update' in request.form:
            book_id = request.form['id']
            book = Book.query.get(book_id)
            book.title = request.form['title']
            book.author = request.form['author']
            db.session.commit()
        elif 'delete' in request.form:
            book_id = request.form['id']
            book = Book.query.get(book_id)
            db.session.delete(book)
            db.session.commit()

    books = Book.query.all()
    return render_template('template_1.html', books=books)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)