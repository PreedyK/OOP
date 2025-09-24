queue = []

def enqueue():
    print("What would you like to add to Queue:")
    queue.append(input("Add to queue"))

def dequeue():
    queue.remove(queue[0])

def display():
    print(queue)

while True:
    print("1. Add to Queue")
    print("2. Remove from Queue")
    print("3. Display Queue")
    print("4. Quit")
    option = input("Select Option:")

    if option == "1":
        enqueue()
    elif option == "2":
        dequeue()

    elif option == "3":
        display()

    elif option == "4":
        break