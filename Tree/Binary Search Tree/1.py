class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BST:
    def __init__(self):
        self.root = None

    def insertion(self, current, data):
        if self.root == None:
            self.root = Node(data)
        else:
            if(data < current.data):
                if(current.leftChild == None):
                    current.leftChild = Node(data)
                else:
                    self.insertion(current.leftChild, data)
            else:
                if (current.rightChild == None):
                    current.rightChild = Node(data)
                else:
                    self.insertion(current.rightChild, data)

    def search(self, key, start):
        if(self.root is None):
            print("BST is empty")
        elif(start):
            if (start.data == key):
                print("Found")
                return
            elif(key < start.data):
                self.search(key, start.leftChild)
            else:
                self.search(key, start.rightChild)
        else:
            print("Not Found")
            return


    def preorder(self, start):
        if(self.root is None):
            print("Tree is empty")
        else:
            if(start):
                print(start.data, end=" ")
                self.preorder(start.leftChild)
                self.preorder(start.rightChild)

    def inorder(self, start):
        if(self.root is None):
            print("BST is empty")
        else:
            if(start):
                self.inorder(start.leftChild)
                print(start.data, end=" ")
                self.inorder(start.rightChild)

    def postorder(self, start):
        if(self.root is None):
            print("BST is empty")
        else:
            if(start):
                self.postorder(start.leftChild)
                self.postorder(start.rightChild)
                print(start.data, end=" ")


bst = BST()
lst = [10, 20, 6, 3, 1]
for i in lst:
    bst.insertion(bst.root, i)

bst.preorder(bst.root)
print()
# bst.inorder(bst.root)
#
# print()
# bst.postorder(bst.root)

bst.search(6, bst.root)
bst.search(906, bst.root)