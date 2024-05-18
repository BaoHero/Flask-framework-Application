import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

path_db = 'E:/Sqlitee/static/Database/books.db'

def get_db():
    conn = sqlite3.connect(path_db)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db()
    c = conn.cursor()

    if request.method == 'POST':
        if 'add' in request.form:
            title = request.form['title']
            author = request.form['author']
            c.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
            conn.commit()
        elif 'update' in request.form:
            book_id = request.form['id']
            title = request.form['title']
            author = request.form['author']
            c.execute('UPDATE books SET title = ?, author = ? WHERE id = ?', (title, author, book_id))
            conn.commit()
        elif 'delete' in request.form:
            book_id = request.form['id']
            c.execute('DELETE FROM books WHERE id = ?', (book_id,))
            conn.commit()

    c.execute('SELECT * FROM books')
    books = c.fetchall()
    conn.close()
    return render_template('template_1.html', books=books)

if __name__ == '__main__':
    
    app.run(debug=True)

