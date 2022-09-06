"""
Single Linked List.
Starting point is called as the Head.
Last point is called as the tail.
Allows moving forward.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertBegin(self, data):
        new_node = Node(data)
        new_node.link = self.head
        self.head = new_node

    def insertEnd(self, data):
        new_node = Node(data)

        # check whether the list is empty
        if(self.head is None):
            new_node.link = self.head
            self.head = new_node
        else:
            n = self.head
            while(n.link is not None):
                n = n.link
            n.link = new_node

    def insertInBetween(self, data, idx):
        new_node = Node(data)

        # check whether the list is empty
        if (self.head is None):
            new_node.link = self.head
            self.head = new_node
        else:
            n = self.head
            for i in range(idx-1):
                n = n.link
            new_node.link = n.link
            n.link = new_node

    def removeBegin(self):

        # case 1: empty list
        # case 2: one or many nodes

        if (self.head is None):
            print("No Node Present")
        else:
            self.head = self.head.link

    def removeEnd(self):

        #case 1: empty list.
        #case 2: one or many nodes are present.
        if(self.head is None):
            print("No Node Present")
        else:
            n = self.head
            while(n.link.link is not None):
                n = n.link
            n.link = None

    def removeInBetween(self, idx):
        # case 1: empty list
        # case 2: one or many nodes
        if(self.head is None):
            print("Empty List. No node is present.")
        else:
            n = self.head
            for i in range(idx-1):
                n = n.link
            n.link = n.link.link


    def traversal(self):
        if(self.head == None):
            print("Linked List is Empty")
        else:
            n = self.head
            while(n is not None):
                print(n.data)
                n = n.link


ll = LinkedList()


while True:
    print("Perform the following Operations in Single Linked List: \n"
          "\t1. Add\n"
          "\t2. Remove\n"
          "\t3. Traversal\n")

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
            ll.insertBegin(data)
        elif(subChoice == 2):
            ll.insertEnd(data)
        elif(subChoice == 3):
            idx = int(input("Enter the index value: "))
            ll.insertInBetween(data, idx)

    elif(choice == 2):
        print("Perform the following Remove Operations: \n"
              "\t1. Begin\n"
              "\t2. end\n"
              "\t3. Inbetween\n"
              )

        subChoice = int(input("Enter your sub-choice: "))

        if (subChoice == 1):
            ll.removeBegin()
        elif (subChoice == 2):
            ll.removeEnd()
        elif (subChoice == 3):
            idx = int(input("Enter the index value: "))
            ll.removeInBetween(idx)

    elif(choice == 3):
        ll.traversal()
    else:
        print("Entered the wrong choice")
        break
