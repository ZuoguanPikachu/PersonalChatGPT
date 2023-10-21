from config import *
import os
import json
import openai
import requests
from simplesqlite import SimpleSQLite
from simplesqlite.query import Where
from flask import Flask, send_file, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO, send, emit
from engineio.async_drivers import gevent


app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, async_mode='gevent', cors_allowed_origins='*')


@app.route('/')
def index():
    return send_file('./webui/index.html')


@app.route('/<path:file>')
def get_file(file):
    return send_file(f'./webui/{file}')


@app.route('/chat-list')
def get_chat_list():
    table_name = "chat_list"
    chat_db_con.create_table(table_name, ["chatId"])
    chat_list = list(map(lambda item: item["chatId"], chat_db_con.select_as_dict(table_name=table_name)))

    return jsonify(chat_list)


@app.route('/add-chat', methods=['POST'])
def add_chat():
    data = request.json
    table_name = "chat_list"
    chat_db_con.create_table(table_name, ["chatId"])
    chat_db_con.insert(table_name, data)
    chat_db_con.commit()
    return "200"


@app.route('/chat-content', methods=['POST'])
def get_chat_content():
    data = request.json
    chat_id = data["chatId"]

    chat_db_con.create_table(chat_id, ["role", "content"])
    chat_content = list(map(lambda item: dict(item), chat_db_con.select_as_dict(table_name=chat_id)))

    return jsonify(chat_content)


@app.route('/save-msg', methods=['POST'])
def save_msg():
    data = request.json
    chat_id = data["chatId"]
    msg = data["msg"]

    chat_db_con.create_table(chat_id, ["role", "content"])
    if len(msg) >= 2:
        chat_db_con.insert_many(chat_id, msg)
    else:
        chat_db_con.insert(chat_id, msg)
    chat_db_con.commit()
    return "200"


@app.route('/remove', methods=['POST'])
def remove():
    data = request.json
    chat_id = data["chatId"]

    chat_db_con.delete("chat_list", Where("chatId", chat_id))
    chat_db_con.drop_table(chat_id)
    chat_db_con.commit()
    return "200"


@app.route('/balance')
def balance_query():
    url = "https://api.chatanywhere.org/v1/query/balance"
    headers = {
        "authorization": API_KEY,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        "origin": "https://api.chatanywhere.org",
        "referer": "https://api.chatanywhere.org/"
    }
    response = requests.post(url, headers=headers)
    content = json.loads(response.content.decode())
    balance = content["balanceTotal"] - content["balanceUsed"]

    return str(balance)


@app.route('/models')
def get_models():
    response = openai.Model.list()
    models = map(lambda item: item["id"], response["data"])
    models = filter(lambda item: item.startswith("gpt"), models)

    return jsonify(list(models))


@app.route('/generate-title', methods=['POST'])
def generate_title():
    messages = request.json["messages"]
    messages.append({"role": "user", "content": "请问上面的对话取一个简短的标题"})

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )
    content = response["choices"][0]["message"]["content"].strip('"')

    return content


@socketio.on('chat')
def chat(data):
    model = data["model"]
    messages = data["msg"]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        stream=True,
    )

    for event in response:
        if event['choices'][0]['finish_reason'] == 'stop':
            emit('bot_response', '[/response_end]')
            break
        for delta_k, delta_v in event['choices'][0]['delta'].items():
            if delta_k == 'content':
                emit('bot_response', delta_v)
                socketio.sleep(0)


if __name__ == '__main__':
    openai.api_key = API_KEY
    openai.api_base = API_BASE

    if not os.path.exists("./db"):
        os.mkdir("db")
    chat_db_con = SimpleSQLite("db/chat_db.sqlite", "a")

    print("Running: http://127.0.0.1:5000")
    socketio.run(app)
