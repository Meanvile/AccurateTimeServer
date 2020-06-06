import socket
from datetime import datetime

s = socket.socket()
s.connect(('127.0.0.1', 123))
print("Клиент в сети...")
while True:
    string = input("Нажмите любую клавишу: ")
    s.send(string.encode())
    if string == "quit":
        break
    print('Настоящее время: ' + str(datetime.now()))
    print("Ложное время: ", s.recv(1024).decode())
print("Завершение процесса...")
s.close()