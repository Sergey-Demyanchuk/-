import socket
import pygame as pg
import math

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)
sock.connect(("localhost",10000))

pg.init()
width,height = 800,600
CC = (width/2,height/2)
radius = 50
screen = pg.display.set_mode((width,height))
pg.display.set_caption(title="Bacteria")
run = True
old = (0,0)
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if pg.mouse.get_focused(): #Проверку на мышку на экране
            pos = pg.mouse.get_pos()
            vector = pos[0] - CC[0],pos[1] - CC[1]
            lenv = math.sqrt(vector[0]**2 + vector[1]**2)
            vector = vector[0]/lenv,vector[1]/lenv


            if lenv <= radius:
                vector = 0,0


    #sock.send("Привет".encode())
            if vector != old:
                old = vector
                message = f"{vector[0]},{vector[1]}"
                sock.send(message.encode())


    data = sock.recv(1024).decode()

    print("Получил!",data)
    screen.fill("grey")
    pg.draw.circle(screen,(255,100,100), CC, radius)
    pg.display.flip()

pg.quit()