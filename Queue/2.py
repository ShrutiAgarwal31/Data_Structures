"""
Implementation of Queue using List Data Structure.
For Enqueue, use insert(0, data) function --> add elements to the 0th index everytime.
For Dequeue, use pop() function --> remove elements from the end.

entering the element from the front and removing from the end.
"""

class Queue:
    def __init__(self, size):
        self.queue = list()
        self.size = size

    def enqueue(self):
        if (len(self.queue) == self.size):
            print("Queue is Full.")
        else:
            data = int(input("Enter a number: "))
            self.queue.insert(0, data)
            print(self.queue)

    def dequeue(self):
        if (len(self.queue) == 0):
            print("Queue is Empty")
        else:
            self.queue.pop()
            print(self.queue)

    def isEmpty(self):
        if(len(self.queue) == 0):
            print("Queue is Empty")
        else:
            print("Queue is not Empty")

    def isFull(self):
        if(len(self.queue) == self.size):
            print("Queue is Full")
        else:
            print("Queue is not Full")

    def peek(self):
        print(self.queue[0])

    def lasElement(self):
        print(self.queue[-1])

size = int(input("Enter the size of the queue: "))
queue = Queue(size)

while True:
    print("Perform the following operations: \n"
          "\t1. Enqueue\n"
          "\t2. Dequeue\n"
          "\t3. IsEmpty\n"
          "\t4. IsFull\n"
          "\t5. Peek Element\n"
          "\t6. Last Element\n"
          "\t7. Quit\n")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        queue.enqueue()

    elif choice == 2:
        queue.dequeue()

    elif choice == 3:
        queue.isEmpty()

    elif choice == 4:
        queue.isFull()

    elif choice == 5:
        queue.peek()

    elif choice == 6:
        queue.lasElement()

    else:
        print("Entered the incorrect choice.")
