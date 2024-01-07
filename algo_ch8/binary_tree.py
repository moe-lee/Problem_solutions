class Node(object) :
    def __init__(self, data = None, left = None, right = None) :
        self.data,self.left,self.right = data,left,right
    def setLeftChild(self, node) :
        self.left = node
    def setRightChild(self, node) :
        self.right = node
    def getLeftChild(self) :
        return self.left
    def getRightChild(self) :
        return self.right
    def __repr__(self) :
        return str(self.data)
    def __str__(self) :
        return str(self.data)
    def __ascii__(self) :
        return str(self.data)
class BinaryTree(object) :
    def __init__(self) :
        self.head = None