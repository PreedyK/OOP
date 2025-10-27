import tkinter
root = tkinter.Tk()
root.resizable(False,False)

myCanvas = tkinter.Canvas(root, bg ="white", height=800, width=800)

shape1 = myCanvas.create_oval(80,600,300,100, fill="red")
shape2 = myCanvas.create_rectangle(50,70,100,100, fill="orange")
shape3 = myCanvas.create_line(0,80,100,70)

myCanvas.pack()
root.mainloop()

