import socket

client = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8080))
print("Введи 'Over' чтобы завершить")
while True:
    inp = input("Введите операцию в \
по форме: ")
    if inp == "Over":
        break
    client.send(inp.encode())
    answer = client.recv(1024)
    history = client.recv(1024)
    print("Ответ " + answer.decode())
    print("История " + history.decode())

client.close()