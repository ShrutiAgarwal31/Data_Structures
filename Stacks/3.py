"""
Implement stack using Deque Module.
Deque is a double-ended queue.
Only one end of the queue id used for push and pop operations.
For push, append method is used.
For pop, pop method is used.
"""

import collections
stack = collections.deque()

while True:
    print("Select the operations:\n "
          "\t1.Push\n"
          "\t2.Pop\n"
          "\t3.Peek\n"
          "\t4.IsEmpty\n"
          "\t5.Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter an integer value: "))
        stack.append(data)
        print(stack)
    elif choice ==2:
        if (len(stack) == 0):
            print("Stack is Empty")
        else:
            stack.pop()
    elif choice == 3:
        if(len(stack)==0):
            print("Stack is Empty")
        else:
            print(stack[-1])
    elif choice == 4:
        if (len(stack) == 0):
            print("Stack is Empty")
        else:
            print("Stack is not Empty")
    else:
        print('Entered the incorrect Choice')
        break

