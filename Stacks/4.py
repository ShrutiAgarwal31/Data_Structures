"""
Implement stack using Queue Module.
For push, put method is used.
For pop, get method is used.

if the stack is empty and you are trying to "pop" the element
then it will go into the blocking stage until the stack gets a
new element. to resolve this timeout is used.
It displays the error message after a particular time.

not stack ==> length of stack is Zero.

"""
import queue

stack = queue.LifoQueue()
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
        stack.put(data)
        print(stack.queue)
    elif choice ==2:
        if (not stack):
            print("Stack is Empty")
        else:
            stack.get(timeout=1)
            print(stack.queue)
    elif choice == 3:
        if(not stack):
            print("Stack is Empty")
        else:
            print(stack.queue[-1])
    elif choice == 4:
        if (not stack):
            print("Stack is Empty")
        else:
            print("Stack is not Empty")
    else:
        print('Entered the incorrect Choice')
        break


