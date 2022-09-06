class Node:
    def __init__(self, data):
        self.data = data
        self.forward = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertBegin(self, data):
        new_node = Node(data)
        if(self.head is None):
            # new_node.forward = self.head
            self.head = new_node
        else:
            new_node.forward = self.head
            self.head.previous = new_node
            self.head = new_node

    def insertEnd(self, data):
        new_node = Node(data)
        if(self.head is None):
            new_node.forward = self.head
            self.head = new_node
        else:
            n = self.head
            while(n.forward is not None):
                n = n.forward
            n.forward = new_node
            new_node.previous = n

    def insertInBetween(self, data, idx):
        new_node = Node(data)
        if(new_node is None):
            new_node.forward = self.head
            self.head = new_node
        else:
            n = self.head
            for i in range(idx-1):
                n = n.forward
            new_node.forward = n.forward
            new_node.previous = n
            n.forward.previous = new_node
            n.forward = new_node

    def deleteBegin(self):
        # case 1: empty list
        # case 2: only one node is present
        # case 3: many nodes are present.
        if(self.head is None):
            print("Ddll is empty")
        if (self.head.forward is None):
            self.head = None
        else:
            self.head = self.head.forward
            self.head.previous = None

    def deleteEnd(self):
        # case 1: empty list
        # case 2: only one node is present
        # case 3: many nodes are present.
        if(self.head is None):
            print("Ddll is empty")
        if(self.head.forward is None):
            self.head = None
        else:
            n = self.head
            while(n.forward.forward is not None):
                n = n.forward
            n.forward = None


    def deleteInBetween(self, idx):
        if(self.head is None):
            print("Ddll is empty")
        else:
            n = self.head
            for i in range(idx-1):
                n = n.forward
            n.forward = n.forward.forward
            n.forward.previous = n

    def traversal(self):
        if(self.head is None):
            print("Ddll is empty")
        else:
            n = self.head
            while(n is not None):
                print(n.data)
                n = n.forward

    def reverse_traversal(self):
        if(self.head is None):
            print("Ddll is empty")
        else:
            n = self.head
            while(n.forward is not None):
                n = n.forward

            while(n is not None):
                print(n.data)
                n = n.previous

dll = DoublyLinkedList()
while True:
    print("Perform the following Operations in Doubly Linked List: \n"
          "\t1. Add\n"
          "\t2. Remove\n"
          "\t3. Traversal\n"
          "\t4. Reverse Traversal\n")

    choice = int(input("Enter your choice: "))
    if(choice == 1):
        print("Perform the following Add Operations: \n"
              "\t1. Begin\n"
              "\t2. end\n"
              "\t3. Inbetween\n"
              )

        subChoice = int(input("Enter your sub-choice: "))
        data = int(input("Enter the data: "))

        if(subChoice == 1):
            dll.insertBegin(data)
        elif(subChoice == 2):
            dll.insertEnd(data)
        elif(subChoice == 3):
            idx = int(input("Enter the index value: "))
            dll.insertInBetween(data, idx)

    elif(choice == 2):
        print("Perform the following Remove Operations: \n"
              "\t1. Begin\n"
              "\t2. end\n"
              "\t3. Inbetween\n"
              )

        subChoice = int(input("Enter your sub-choice: "))

        if (subChoice == 1):
            dll.deleteBegin()
        elif (subChoice == 2):
            dll.deleteEnd()
        elif (subChoice == 3):
            idx = int(input("Enter the index value: "))
            dll.deleteInBetween(idx)

    elif(choice == 3):
        dll.traversal()

    elif(choice == 4):
        dll.reverse_traversal()
    else:
        print("Entered the wrong choice")
        break


# ddll =DoublyLinkedList()
# ddll.insertBegin(1)
# ddll.insertBegin(2)
# ddll.insertEnd(3)
# ddll.insertEnd(4)
# ddll.insertInBetween(55, 1)
# ddll.deleteBegin()
# ddll.deleteEnd()
# ddll.traversal()
# print()
# ddll.deleteInBetween(1)
# ddll.traversal()
# ddll.reverse_traversal()
# ddll.deleteBegin()
# ddll.traversal()
"""
2
55
1
3
4
"""