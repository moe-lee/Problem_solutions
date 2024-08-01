from collections import deque
class Node :
    def __init__(self, value = 0, left = None, right = None) :
        self.value = value
        self.left = left
        self.right = right

class BinaryTree :
    def __init__(self) :
        self.root = None

def maxDepth(root) :
    if root is None :
        return 0
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    max_depth = max(right, left) + 1
    return max_depth

def BFS(root) :
    if root is None : return None
    queue = deque()
    queue.append(root)
    visited = []
    while queue :
        cur_node = queue.popleft()
        if cur_node.left : queue.append(cur_node.left)
        if cur_node.right : queue.append(cur_node.right)
        visited.append(cur_node)
    return visited

def DFS(root) :
    if root is None :
        return
    # 여기서 작업 : Preorder traversal
    # print(root.value)
    DFS(root.left)
    # 여기서 작업 : Inorder traversal
    # print(root.value)
    DFS(root.right)
    # 여기서 작업 : Postorder traversal
    print(root.value, end=" ")

def LCA(root, p, q) :
    if root is None :
        return None
    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q) 
    
    if root.value == p or root.value == q :
        return root
    elif left and right :
        return root
    return left or right

def MaximumDepth(root) :
    max_depth = 0
    if root is None :
        return max_depth
    q = deque()
    q.append((root, 1))
    while q :
        cur_node, cur_depth = q.popleft()
        max_depth = max(max_depth, cur_depth)
        if cur_node.left :
            q.append((cur_node.left, cur_depth + 1))
        if cur_node.right :
            q.append((cur_node.right, cur_depth + 1))
    return max_depth

def MaximumDepthDFS(root) :
    max_depth = 0
    if root is None : return max_depth
    left = MaximumDepthDFS(root.left)
    right = MaximumDepthDFS(root.right)
    max_depth = max(left, right) + 1
    return max_depth

bt = BinaryTree()
bt.root = Node(value='A')
bt.root.left = Node(value='B')
bt.root.right = Node(value='C')
bt.root.left.left = Node(value='D')
bt.root.left.right = Node(value='E')
bt.root.right.left = Node(value='F')
bt.root.right.right = Node(value='G')
bt.root.left.left.left = Node(value='H')
bt.root.left.right.left = Node(value='I')
bt.root.left.right.right = Node(value='J')
bt.root.left.right.left.left = Node(value='N')
bt.root.left.right.right.left = Node(value='O')
bt.root.left.right.right.right = Node(value='P')
bt.root.right.left.right = Node(value='K')
bt.root.right.right.left = Node(value='L')
bt.root.right.right.right = Node(value='M')
bt.root.right.right.right.left = Node(value='Q')

print(MaximumDepthDFS(bt.root))