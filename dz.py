from tkinter import *
root=Tk()
root.title('Графические примитивы')

def change():
   canv.itemconfig(square, fill='purple')
   print(canv.itemcget(square, 'fill'))

def change_2():
   canv.itemconfig(sun, fill='red')
   print(canv.itemcget(sun, 'fill'))

def change_1():
   canv.itemconfig(roof, fill='green')
   print(canv.itemcget(roof, 'fill'))

canv=Canvas(root,width=500,height=500,bg="lightblue")
square = canv.create_rectangle(20,150,300,450,fill="green",outline="black")
roof = canv.create_polygon([20,150],[160,30],[300,150],fill="blue",outline="blue")
sun = canv.create_oval(400,10,480,80,fill="yellow",outline="yellow")
canv.pack()

Button(text='1', command=change).pack()
Button(text='2', command=change_1).pack()
Button(text='3', command=change_2).pack()
root.mainloop()

