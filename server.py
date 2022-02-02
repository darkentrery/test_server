import socket
import json
from random import random, randint

def create_table():#функция создания произвольной таблицы
    len_list = 1000000
	#[{id: {col_1: value, col_2: value, col_3: value}}]
    table = [{random(): {1: random(), 2: random(), 3: random()}} for x in range(len_list)]
    table.sort(key=lambda x: list(x.keys())[0], reverse=False)
    return table

def update_table(table):#иммитация обновления таблицы согласно заданным условиям
    for r in range(randint(1, 20)):
        table.append({random(): {1: random(), 2: random(), 3: random()}})
    for r in range(randint(1, 20)):
        del table[r + randint(0, 1000)]
    for r in range(randint(0, 100)):
        table[r] = {random(): {1: random(), 2: random(), 3: random()}}
    table.sort(key=lambda x: list(x.keys())[0], reverse=False)

def server(table):#вызов сервера
	listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	IP = socket.gethostbyname(socket.gethostname())
	PORT = 12333
	listener.bind((IP, PORT))
	listener.listen(10)
	connection, address = listener.accept()
	connection.send("Клиент подключен к серверу!".encode('utf8'))

	while True:
		update_table(table)
		position = connection.recv(1024).decode("utf8")
		position = list(position.split(","))
		n, N = tuple(map(lambda x: int(x), position))
		tab_js = json.dumps(table[n:n+N])
		connection.sendall(tab_js.encode('utf8'))


table = create_table()

server(table)


