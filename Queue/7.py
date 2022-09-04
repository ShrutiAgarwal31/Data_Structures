"""
Priority Queue.
Element is removed according to their priority.
Set priority in two ways:
    1. value of the element as the priority --> lowest element has the lowest priority or the least number has the higher priority
    2. input value and priority in tuple --> (priority, element)
Implement using list
Priority will be in the tuple format.
"""
class PQ:
    def __init__(self, size):
        self.queue = list()
        self.size = size

    def enqueue(self):
        if(len(self.queue) == self.size):
            print("Queue is Full.")
        else:
            priority = int(input("Enter the priority: "))
            data = input("Enter the data: ")
            self.queue.append((priority, data))
            print(self.queue)

    #assumption: lower the priotity number --> higher the priority
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
