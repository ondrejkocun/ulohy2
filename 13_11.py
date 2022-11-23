import tkinter
import random
canvas = tkinter.Canvas(bg = "white")
canvas.pack()

def hocico():
    canvas.delete("all")
    global x,y
    slovo=entry1.get()+" "
    x=50
    y=100
    for i in range(len(slovo)):
        canvas.create_text(x,y,text=slovo[i],font='Arial 30',fill='blue',tags='rytmus')
        x+=30
        canvas.after(1000)
        canvas.update()
    canvas.delete('rytmus')
    canvas.after(3000,hocico)

button1 = tkinter.Button(text='saudska arabia', command = hocico)
button1.pack()
entry1 = tkinter.Entry()
entry1.pack()
