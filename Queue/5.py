"""
Priority Queue.
Element is removed according to their priority.
Set priority in two ways:
    1. value of the element as the priority --> lowest element has the lowest priority or the least number has the higher priority
    2. input value and priority in tuple --> (element, priority)
Implement using list or PriorityQueue Model
For implementing using the list, sort the queue.
"""
class PQ:
    def __init__(self, size):
        self.queue = list()
        self.size = size

    def enqueue(self):
        if(len(self.queue) == self.size):
            print("Queue is Full.")
        else:
            data = int(input("Enter the data: "))
            self.queue.append(data)
            print(self.queue)

    #assumption: lower the number --> higher the priority
    def dequeue(self):
        if(len(self.queue) == 0):
            print("Queue is Empty")
        else:
            self.queue.sort()
            self.queue.pop(0)
            print(self.queue)

size = int(input("Size of the Priority Queue: "))
queue = PQ(size)

while True:
    print("Perform the following operations: \n"
          "\t1. Enqueue\n"
          "\t2. Dequeue\n")

    choice = int(input("Enter your choice: "))

    if(choice == 1):
        queue.enqueue()
    elif(choice == 2):
        queue.dequeue()
    else:
        print("Entered the wrong choice.")
        break
