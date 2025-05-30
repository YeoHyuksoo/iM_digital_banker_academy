import socket
import json

host = "127.0.0.1"
port = 5050

while True:
    print("질문 : ")
    query = input()
    if (query == "exit"):
        exit(0)
    print("-" * 40)

    mySocket = socket.socket() # 클라이언트에서 사용할 소켓 생성
    mySocket.connect((host, port)) # 서버에게 연결 요청

    json_data = {
        'Query': query,
        'BotType': "MyService"
    }
    message = json.dumps(json_data)
    mySocket.send(message.encode()) # 메세지 송신

    data = mySocket.recv(2048).decode() # 서버가 보낸 메세지 수신
    ret_data = json.loads(data)
    print("답변 : ")
    print(ret_data['Answer'])
    print(ret_data)
    print(type(ret_data))
    print("\n")
    mySocket.close()