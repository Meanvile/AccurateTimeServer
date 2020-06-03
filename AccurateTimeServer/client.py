import socket
import datetime

s = socket.socket()
s.connect(('127.0.0.1', 123))
while True:
    string = input("Нажмите любую клавишу: ")
    s.send(string.encode())
    if string == "quit":
        break
    curr_time = datetime.datetime.now()
    print('Настоящее время: ' + str(curr_time))
    print("Ложное время: ", s.recv(1024).decode())
s.close()