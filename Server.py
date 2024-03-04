import time
import socket

main_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#Настройка сокета

main_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)#Отключение пакетирование
main_socket.bind(("localhost",10000))#Привязка айпи к порту
main_socket.setblocking(False)#Настраиваем непрерывность
main_socket.listen(5)#Количество участников
print("Сокет создался")
players = []
while True:
    try:
    #Проверяем желающий присоединиться
        new_socket, addr = main_socket.accept()#Принимаем входящие данные
        print("Подключился!", addr)
        new_socket.setblocking(False)
        players.append(new_socket)
    except BlockingIOError:
        pass
#Подсчёт комманды игроков
for sock in players:
    try:
        data = sock.recv(1024).decode() #Обработка сообщений по 1024 байта
        print("Получил", data)
    except:
        pass
