import tkinter as tk
from turtledemo.sorting_animate import show_text

top = tk.Tk()
top.geometry("700x700")

add = tk.Entry(top, width=35)
add.place(x=100, y=100)

class Queue:
    def __init__(self):
        self.element = []

    def enqueue(self):
        x = q_valueTxt.get(1.0, "end-1c").strip()
        if x:
            self.element.append(x)
            q_valuetxt.delete(1.0, "end")
        else:
            print("Please Enter a Value First.")

    def dequeue(self):
        self.element.remove(0)

    def display_queue(self):
        print("Elements in Queue:")
        for i in self.element:
            print(i)
        print()


class Stack:
    def __init__(self):
        self.element = []

    def push(self):
        value = s_text_Box.get(1.0, "end-1c").strip()
        if value:
            self.element.append(value)
            s_text_Box.delete(1.0, "end")
        else:
            print("Please Enter a Value First.")

    def pop(self):
        self.element.pop()

    def display_stack(self):
        print("Elements in Stack:")
        for i in self.element:
            print(i)


#Main Code
q1 = Queue()
q2 = Queue()

B1 = tk.Button(top, text="Create Queue", width=10, height=5)
B1.place(x=100, y=150)

B2 = tk.Button(top, text="Enqueue", width=10, height=5, command=q1.enqueue)
B2.place(x=200, y=150)

B3 = tk.Button(top, text="Dequeue", width=10, height=5, command=q1.dequeue)
B3.place(x=300, y=150)

B4 = tk.Button(top, text="Display Queue", width=10, height=5, command=q1.display_queue)
B4.place(x=400, y=150)

top.mainloop()

s1 = Stack()
s2 = Stack()

s1.push()
s1.pop()
s1.display_stack()
