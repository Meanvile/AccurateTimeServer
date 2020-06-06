import socket
from datetime import datetime, timedelta

s = socket.socket()
s.bind(('localhost', 123))
s.listen(5)
print("Cервер работает...")
c, addr = s.accept()
while True:
    recv = c.recv(4096).decode()
    if recv == "quit":
        break
    deceit_time = int(open('config.txt').read().strip())
    callback = str((datetime.now() + timedelta(seconds=deceit_time)))
    c.send(callback.encode())
print('Произошло отключение сервера')
s.close()
