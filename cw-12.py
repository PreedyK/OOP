import tkinter as tk

top = tk()
top.geometry("700x700")

add = tk.Text(width=35, height=2)
add.place(x=100, y=100)

class Queue:
    def __init__(self):
        self.element = []

    def enqueue(self):
        valueTxt = tk.Text(top,width = 35, height = 2)
        x = valueTxt.get(1.0, "end-1c")

        self.element.append(input("Enter a Value:"))

    def dequeue(self):
        self.element.remove(0)

    def display_queue(self):
        print("Elements in Queue:")
        for i in self.element:
            print(i)


B1 = tk.Button(top, text="Create Queue", width=10, height=5, command=lambda: show("1"))
B1.place(x=100, y=150)

B2 = tk.Button(top, text="Enqueue", width=10, height=5, command=lambda: show("1"))
B2.place(x=100, y=150)

B3 = tk.Button(top, text="Dequeue", width=10, height=5, command=lambda: show("1"))
B3.place(x=100, y=150)

B4 = tk.Button(top, text="Display Queue", width=10, height=5, command=lambda: show("1"))
B4.place(x=100, y=150)

#Main
q1 = Queue()
q2 = Queue()