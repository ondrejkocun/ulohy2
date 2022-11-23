import tkinter
import random
canvas = tkinter.Canvas(bg = "white")
canvas.pack()

def hocico():
    canvas.delete("all")
    slovo=entry1.get()
    x=50
    y=50
    for i in range(len(slovo)):
        farba=random.choice(("red","green","blue","yellow","black","purple","orange"))
        canvas.create_text(x,y,text=slovo[i],font="Arial 10",fill=farba)
        x+=15

button1 = tkinter.Button(text='saudska arabia', command = hocico)
button1.pack()
entry1 = tkinter.Entry()
entry1.pack()
