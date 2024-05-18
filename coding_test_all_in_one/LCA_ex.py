from collections import deque
def LCA(root, p, q) :
    if root == None:
        return None
    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)
    
    if root == p or root == q :
        return root
    elif left and right :
        return root
    return left or right


def maxDepth_BFS(root) :
    q = deque()
    max_depth = 0
    if root == None :
        return max_depth
    q.append((root, 1))
    while q :
        cur_node, cur_depth = q.popleft()
        max_depth = max(max_depth, cur_depth)
        if cur_node.left :
            q.append((cur_node.left, cur_depth+1))
        if cur_node.right :
            q.append((cur_node.right, cur_depth+1))
    return max_depth

def maxDepth_DFS(root) :
    if root == None :
        return 0
    left = maxDepth_DFS(root.left)
    right = maxDepth_DFS(root.right)
    
    return max(left, right) + 1
