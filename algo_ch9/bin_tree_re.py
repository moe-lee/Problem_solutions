from binarytree import build, Node

def traversal(node) :
    if node :
        print("Preorder : %d"%node.value)
        traversal(node.left)
        print("Inorder : %d"%node.value)
        traversal(node.right)
        print("Postorder: %d"%node.value)


root = build([1, 2, 3, 4, 5, None, 6])

traversal(root)
