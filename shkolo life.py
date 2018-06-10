import winsound as w
from tkinter import *
from tkinter import messagebox as msg
import os

tk = Tk()
c = Canvas(tk,height = 500,width = 1000,bg = 'black')
c.pack()
tk.resizable(0,0)
tk.title("shkolo life")

bgl = ['grass.gif','floor.gif']

grass1 = PhotoImage(file = bgl[0])
grass = c.create_image(0,0,anchor = NW,image = grass1)


w.PlaySound('1.wav',w.SND_ASYNC)


ps = 5


player1 = PhotoImage(file = 'player.gif')
player2 = c.create_image(0,0,anchor= NW,image = player1)

car1 = PhotoImage(file = 'car.gif')
car2 = c.create_image(100,200,anchor = NW,image = car1)
door1 = PhotoImage(file = 'door.gif')
door = c.create_image(300,100,anchor=NW,image= door1)
dp = c.coords(door)

pp = c.coords(player2)

def use():
    global floor1
    global floor
    global player1
    global player2
    global door1
    global door
    global shk1
    global shk
    global b
    global bi
    
    
    dp = c.coords(door)
    pp = c.coords(player2)
    if pp[0] == dp[0] and pp[1] == dp[1]:

        try:
            c.delete(floor)
            c.delete(shk)
            c.delete(bi)
            del floor1
            del shk1
            del b
##            floor1 = PhotoImage(file = bgl[1])
##            floor = c.create_image(0,0,anchor = NW,image = floor1)
            
        except:
            global player
            floor1 = PhotoImage(file = bgl[1])
            floor = c.create_image(0,0,anchor = NW,image = floor1)
            player1 = PhotoImage(file = 'player.gif')
            player2 = c.create_image(300,100,anchor= NW,image = player1)
            door1 = PhotoImage(file  = 'door.gif')
            door = c.create_image(300,100,anchor = NW, image = door1)
            shk1= PhotoImage(file = 'shk.gif')
            shk = c.create_image(400,100,anchor=NW,image=shk1)
            msg.showinfo("WAT?","Что ти туты дилаишь?")
            msg.showerror("!!!","Тiкай с гхороду!")
            c.delete(floor)
            c.delete(shk)
            del floor1
            del shk1
 
            c.delete("all")

            w.PlaySound('2.wav',w.SND_ASYNC)
            b = PhotoImage(file = 'b.gif')
            bi = c.create_image(0,0,anchor=NW,image=b)
            player2 = c.create_oval(10,10,60,60,fill = 'lime')
        
        
def control(event):
    if event.keysym == 'Right':
        c.move(player2,ps,0)
    if event.keysym == 'Left':
        c.move(player2,-ps,0)
    if event.keysym == 'Up':
        c.move(player2,0,-ps)
    if event.keysym == 'Down':
        c.move(player2,0,ps)
    if event.keysym == 'e':
        use()

    pp = c.coords(player2)
        

c.bind_all('<KeyPress-Right>',control)
c.bind_all('<KeyPress-Left>',control)
c.bind_all('<KeyPress-Up>',control)
c.bind_all('<KeyPress-Down>',control)
c.bind_all('<KeyPress-e>',control)
