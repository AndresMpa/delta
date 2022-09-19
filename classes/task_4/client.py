import socket
import json

client_socket = socket.socket()

client_socket.connect(("localhost", 8000))

print("Client ready to chatting")

while True:
    message = input('> ')

    client_socket.send(message.encode('utf-8'))

    raw_answer = client_socket.recv(1024).decode('utf-8')
    answer = json.loads(raw_answer)

    print(answer)

    if message == "end":
        print("Chat ended")
        client_socket.close()
        break
