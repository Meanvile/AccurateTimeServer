<b>Задание №2 - Сервер точного времени, который врёт на заданное количество секунд.</b>

Серверу поступает запрос от клиента, о желании узнать время. Сервер спрашивает точное время у операционной системы и
прибавляет к нему заданное в конфигурационном файле количество секунд, после этого отправляет эти данные клиенту.<br><br>
Чтобы запустить вводим: python server.py - для запуска сервера, python client.py - для запуска клиента.<br><br>
В клиенте можно вводить любую комбинацию, после чего нужно нажать enter, чтобы отправить запрос и получить ответ.<br><br> 
Для того, чтобы задать время, на которое сервер будет нам врать, открываем config.txt и вводим нужное количество секунд.
