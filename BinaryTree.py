from collections import deque

class Node :
    def __init__(self, value, left = None, right = None) :
        self.value = value
        self.left = left
        self.right = right
    
class BinaryTree :
    def __init__(self) :
        self.root = None


def bfs(root) :
    # 방문하여 하는 작업은 visited 리스트에 노드를 추가하는 것.
    visited = []
    q = deque()
    if root is None :
        return visited
    q.append(root)
    
    while q:
        cur_node = q.popleft()
        visited.append(cur_node)
        if cur_node.left : q.append(cur_node.left)
        if cur_node.right : q.append(cur_node.right)
    
    return visited

def dfs(root):
    if root is None:
        return
    dfs(root.left)
    dfs(root.right)

def preorder(cur_node) :
    if cur_node is None :
        return
    print(cur_node.value)
    preorder(cur_node.left)
    preorder(cur_node.right)

def inorder(cur_node) :
    if cur_node is None :
        return
    inorder(cur_node.left)
    print(cur_node.value)
    inorder(cur_node.right)

def postorder(cur_node) :
    if cur_node is None :
        return
    postorder(cur_node.left)
    postorder(cur_node.right)
    print(cur_node.value)


def bfs(root) :
    q = deque()
    visited = []
    if root is None :
        return visited
    q.append(root)
    
    while q:
        cur_node = q.popleft()
        visited.append(cur_node)
        if cur_node.left : q.append(cur_node.left)
        if cur_node.right : q.append(cur_node.right)
    return visited

def dfs(root) :
    if root is None :
        return None
    dfs(root.left)
    dfs(root.right)

def LCA(root, p, q) :
    if root is None : return None
    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)
    
    if root == q or root == p :
        return root
    elif left and right :
        return root
    return left or right

def LCA(root, p, q) :
    if root is None:
        return None
    left =LCA(root.left, p, q)
    right =LCA(root.right, p, q)
    if root == p or root == q:
        return root
    elif left and right:
        return root
    else :
        return left or right

print(LCA([3,5, 1, 6, 2, 0, 8, None, None, 7, 3], 6, 4))
