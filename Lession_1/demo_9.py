from flask import Flask, request

app = Flask(__name__)

# Tạo một dictionary đơn giản để simulating dữ liệu tìm kiếm
data = {
    'apple': 'Quả táo',
    'banana': 'Quả chuối',
    'orange': 'Quả cam',
    'grape': 'Quả Nho',
    'watermelon': 'Quả dưa hấu'
}

@app.route('/search')
def search():
    # Lấy query string từ URL
    keyword = request.args.get('keyword')

    # Kiểm tra xem từ khoá tìm kiếm có tồn tại trong data không
    if keyword in data:
        result = data[keyword]
    else:
        result = 'Không tìm thấy kết quả cho từ khoá "{}"'.format(keyword)

    return result

if __name__ == '__main__':
    app.run(debug=True)

"""
try this:

http://127.0.0.1:5000/search?keyword=orange
http://127.0.0.1:5000/search?keyword=lemon
"""