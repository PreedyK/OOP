import tkinter as tk

top = tk.Tk()
top.geometry("700x700")

add = tk.Entry(top, width=35)
add.place(x=100, y=100)

class Queue:
    def __init__(self):
        self.element = []

    def enqueue(self):
        valueTxt = tk.Text(top,width = 35, height = 2)
        valueTxt.place(x=100, y=100)

        def add_value():
            x = valueTxt.get(1.0, "end-1c").strip()
            if x:
                self.element.append(x)
                valueTxt.destroy()
                tk.Button.destroy()

        Button = tk.Button(top, text="add", width=10, height=2, command=add_value)
        Button.place(x=400, y=95)

    def dequeue(self):
        self.element.remove(0)

    def display_queue(self):
        print("Elements in Queue:")
        for i in self.element:
            print(i)
        print()


B1 = tk.Button(top, text="Create Queue", width=10, height=5)
B1.place(x=100, y=150)

B2 = tk.Button(top, text="Enqueue", width=10, height=5)
B2.place(x=100, y=150)

B3 = tk.Button(top, text="Dequeue", width=10, height=5)
B3.place(x=100, y=150)

B4 = tk.Button(top, text="Display Queue", width=10, height=5)
B4.place(x=100, y=150)

#Main
q1 = Queue()
q2 = Queue()
