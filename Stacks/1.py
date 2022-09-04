"""
Implement Stacks using List.
analogy:
for push use append function of the list.
for pop use the pop function of the list.
both push and pop are done at the same end of the list i.e the end of the list.

"""

stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

stack.append(40)
stack.append(50)

print(stack)
print('the top element: ', stack[-1])