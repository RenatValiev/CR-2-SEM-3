import socket
server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8080))
server.listen(1)
print("Сервер запущен")
print("Ожидание ответа клиента")

clientConnection, clientAddress = server.accept()
print("Слиент подключен :", clientAddress)
msg = ''
results = []
counter = 1
while True:

    data = clientConnection.recv(1024)
    msg = data.decode()
    if msg == 'Over':
        print("Подключение закончено")
        break

    print("Получено уравнение")
    result = 0
    operation_list = msg.split()
    oprnd1 = operation_list[0]
    operation = operation_list[1]
    oprnd2 = operation_list[2]


    num1 = int(oprnd1)
    num2 = int(oprnd2)

    if operation == "+":
        result = num1 + num2
    elif operation == "-":

        result = num1 - num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "*":
        result = num1 * num2

    print("Отправить результат клиенту")
    results.append(f"{result} операция номер {counter}" )
    output = str(result)
    clientConnection.send(output.encode())
    clientConnection.send(str(results).encode())
    counter += 1
clientConnection.close()