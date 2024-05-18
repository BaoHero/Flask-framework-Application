from flask import Flask, render_template, request 
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
from threading import Thread

app = Flask(__name__)

# Khởi tạo chatbot
chatbot = ChatBot("CustomChatBot")

# Load dữ liệu từ file .txt và phân chia thành các cặp câu hỏi và câu trả lời
conversations = []
with open("data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    i = 0
    while i < len(lines):
        question = lines[i].strip()
        i += 1
        answer = lines[i].strip()
        i += 1
        conversations.append(question)
        conversations.append(answer)

# Tạo bộ đào tạo tùy chỉnh và huấn luyện chatbot
trainer = ListTrainer(chatbot)
trainer.train(conversations)

@app.route("/")
def log():
    return f'''
        <body style="display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background-color: #f0f0f0;">
        <button onclick="window.location.href='/chatbot'" style="padding: 15px 25px; background-color: #4CAF50; color: white; border: none; border-radius: 8px; cursor: pointer; font-size: 30px; text-align: center; text-decoration: none; display: inline-block; transition: transform 2s;">Chat với chăm sóc khách hàng</button>

    '''

@app.route("/chatbot")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    time.sleep(1)
    user_text = request.args.get("msg")
    # Tạo một luồng mới để xử lý bot's response và trả về
    response_thread = Thread(target=lambda: get_bot_response(user_text))
    response_thread.start()
    return str(chatbot.get_response(user_text))

if __name__ == "__main__":
    app.run(debug=True)
