import tkinter
import random
canvas = tkinter.Canvas(bg = "white")
canvas.pack()
osamabinladin=0
def hocico():
    global osamabinladin
    canvas.delete("all")
    slovo=entry1.get()
    x=50
    y=50
    for i in range(len(slovo)):
           canvas.create_text(x,y-10,text=slovo[i],angle=osamabinladin,font='Arial 10')
           osamabinladin=osamabinladin+(360/len(slovo)-1)
           x+=15

button1 = tkinter.Button(text='saudska arabia', command = hocico)
button1.pack()
entry1 = tkinter.Entry()
entry1.pack()
