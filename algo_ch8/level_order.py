from collections import deque as queue
import binary_tree

def preorder(root) :
    stack = queue()
    stack.append(root)
    while stack :
        node = stack.pop()
        if node :
            stack.append(node.getRightChild())
            stack.append(node.getLeftChild())
            print(node)
    return

def level_ordering(root) :
    parents = queue()
    childs = queue()
    parents.append(root)
    node_by_level = []
    print(parents)
    while parents or childs :
        node_by_level.append([])
        while parents:
            node = parents.popleft()
            if node :
                node_by_level[-1].append(node)
                childs.append(node.getLeftChild())
                childs.append(node.getRightChild())
        parents = childs
        childs = queue()
    return node_by_level

def level_ordering_app1(root) :
    parents = queue()
    parents.append(root)
    childs = queue()
    node_by_level = []
    while parents :
        node_by_level.append([])
        sorting_queue = queue()
        while parents :
            node = parents.popleft()
            if node :
                sorting_queue.append(node)
                childs.append(node.getLeftChild())
                childs.append(node.getRightChild())
        while sorting_queue : node_by_level[-1].append((sorting_queue.popleft()) if len(node_by_level) % 2 else (sorting_queue.pop()))
        parents = childs
        childs = queue()
    return node_by_level

def level_ordering_app2(root) :
    parents = queue()
    parents.append(root)
    childs = queue()
    node_by_level = []
    level_stack = queue()
    while parents :
        this_level = []
        while parents :
            node = parents.popleft()
            if node :
                this_level.append(node)
                childs.append(node.getLeftChild())
                childs.append(node.getRightChild())
        level_stack.append(this_level)
        parents = childs
        childs = queue()
    level_stack.pop()
    while level_stack :
        node_by_level.append(level_stack.pop())
    return node_by_level

def level_ordering_app3(root) :
    parents = queue()
    childs = queue()
    parents.append(root)
    avg_value_by_level = []
    while parents or childs :
        cnt_this_level = 0
        sum_this_level = 0
        while parents:
            node = parents.popleft()
            if node :
                cnt_this_level +=1
                sum_this_level += node.data
                childs.append(node.getLeftChild())
                childs.append(node.getRightChild())
        if cnt_this_level : avg_value_by_level.append(sum_this_level / cnt_this_level)
        
        parents = childs
        childs = queue()
    return avg_value_by_level

if __name__ == "__main__" :
    root = binary_tree.Node(314)
    n1 = binary_tree.Node(6)
    n2 = binary_tree.Node(6)
    n3 = binary_tree.Node(271)
    n4 = binary_tree.Node(561)
    n5 = binary_tree.Node(2)
    n6 = binary_tree.Node(271)
    n7 = binary_tree.Node(28)
    n8 = binary_tree.Node(0)
    n9 = binary_tree.Node(3)
    n10 = binary_tree.Node(1)
    n11 = binary_tree.Node(28)
    n12 = binary_tree.Node(17)
    n13 = binary_tree.Node(401)
    n14 = binary_tree.Node(257)
    n15 = binary_tree.Node(641)
    n16 = binary_tree.Node(777)
    root.setLeftChild(n1)
    root.setRightChild(n2)
    n1.setLeftChild(n3)
    n1.setRightChild(n4)
    n2.setLeftChild(n5)
    n2.setRightChild(n6)
    n3.setLeftChild(n7)
    n3.setRightChild(n8)
    n4.setRightChild(n9)
    n5.setRightChild(n10)
    n6.setRightChild(n11)
    n9.setLeftChild(n12)
    n10.setLeftChild(n13)
    n10.setRightChild(n14)
    n13.setRightChild(n15)
    print(level_ordering_app3(root))