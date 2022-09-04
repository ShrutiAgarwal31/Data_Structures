stack = []
class Stack:
    def __init__(self):
        self.stack = list()

    def push(self):
        element = int(input("Enter a integer value: "))
        self.stack.append(element)
        print(self.stack)

    def pop(self):
        if(len(self.stack)==0):
            print('Stack is Empty')
        else:
            self.stack.pop()
        print(self.stack)

    def peek(self):
        if (len(self.stack) == 0):
            print('Stack is Empty')
        else:
            print(self.stack[-1])
            
    def isEmpty(self):
        if(len(self.stack)==0):
            print('Stack is Empty')
        else:
            print("Stack is not Empty")

stack = Stack()
while True:
    print("Select the operations:\n "
          "\t1.Push\n"
          "\t2.Pop\n"
          "\t3.Peek\n"
          "\t4.IsEmpty\n"
          "\t5.Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        stack.push()
    elif choice ==2:
        stack.pop()
    elif choice == 3:
        stack.peek()
    elif choice == 4:
        stack.isEmpty()
    else:
        print('Entered the incorrect Choice')
        break

