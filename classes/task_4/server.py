import datetime
import socket
import json

# Socket creation
server_socket = socket.socket()

server_socket.bind(("localhost", 8000))
server_socket.listen(1)

cli, addr = server_socket.accept()

print("Server ready to chatting")

while True:
    date = datetime.datetime.now()
    raw_message = cli.recv(1024).decode("utf-8")
    connection = {
        "message": raw_message,
        "Time": date.strftime('%A'),
        "Hour": date.strftime('%X'),
        "Port": str(addr[1]),
        "IP": str(addr[0]),
    }

    message = json.dumps(connection)

    cli.send(message.encode())
    print(message)

    if raw_message == "end":
        break

cli.close()
server_socket.close()
