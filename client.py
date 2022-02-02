import socket
import json

def client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP = socket.gethostbyname(socket.gethostname())
    PORT = 12333
    client.connect((IP, PORT))
    data = client.recv(1024).decode('utf8')
    print(data)
    while True:
        # передача значений скролинга - 2 числа через запятую.
        #1 - номер строки - положение скроллера
        #2 - высота окна
        print("Введите номер первойстрок и высоту таблицы по форме '1,2':")
        position = input()
        position = bytearray(position, 'utf-8')
        client.send(position)

        data = ''
        while True:
            d = client.recv(1024).decode('utf8')
            data += d
            if d.__sizeof__() < 1024:
                break
        data = json.loads(data)
        for d in data:
            print(d)

    client.close()

client()