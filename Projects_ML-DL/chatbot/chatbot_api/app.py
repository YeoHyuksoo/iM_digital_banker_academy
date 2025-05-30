from flask import Flask, request, jsonify, abort, render_template

import socket
import json

host = "127.0.0.1"
port = 5050

app = Flask(__name__)

def get_answer_From_engine(bottype, query):
    mySocket = socket.socket()
    mySocket.connect((host, port))
    json_data = {
        'Query': query,
        'BotType': bottype
    }
    message = json.dumps(json_data)
    mySocket.send(message.encode())

    data = mySocket.recv(2048).decode()
    ret_data = json.loads(data)

    mySocket.close()
    return ret_data

@app.route('/', methods = ['GET'])
def index():
    return render_template("index.html")

@app.route('/query/<bot_type>', methods = ['POST'])
def query(bot_type):
    print("bot_type :", bot_type)
    body = request.get_json()
    print(body)
    try:
        if bot_type == 'WEB':
            ret = get_answer_From_engine(bottype = bot_type, query = body['query'])
            print(ret)
            return jsonify(ret)
        else:
            abort(404)

    except Exception as ex:
        abort(500)

if __name__ == "__main__":
    app.run(host = '127.0.0.1', port = 5000)