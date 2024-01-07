import binary_tree
from collections import deque as queue

def preorder(root, deapth, look_up_tbl) :
    if root is None : return
    look_up_tbl.append((deapth, root));
    preorder(root.getLeftChild(), deapth+1, look_up_tbl)
    preorder(root.getRightChild(), deapth+1, look_up_tbl)

def depth_order(root) :
    depth_tbl = list()
    preorder(root, 0, depth_tbl)
    result = sorted(depth_tbl, key = lambda x : x[0])
    result = list(map(lambda x : x[1], result))
    return result

def depth_order2(root) :
    result = []
    parent = queue()
    parent.append(root)
    while parent :
        this_level = []
        child = queue()
        while parent :
            node = parent.popleft()
            if node :
                this_level.append(node)
                child.append(node.getLeftChild())
                child.append(node.getRightChild())
        result.append(this_level)
        parent = child
    return result

def depth_order3(root) :
    result = []
    parent = queue()
    parent.append(root)
    while parent :
        this_level = []
        buffer = queue()
        child = queue()
        while parent :
            node = parent.popleft()
            if node :
                buffer.append(node)
                child.append(node.getLeftChild())
                child.append(node.getRightChild())
        while buffer:
            if(len(result) & 1) : this_level.append(buffer.pop())
            else : this_level.append(buffer.popleft())
        if this_level: result.append(this_level)
        parent = child
    return result


def depth_order4(root) :
    result = []
    parent = queue()
    parent.append(root)
    depth_stack = queue()
    
    while parent :
        this_level = []
        child = queue()
        while parent :
            node = parent.popleft()
            if node :
                this_level.append(node)
                child.append(node.getLeftChild())
                child.append(node.getRightChild())
        if this_level: depth_stack.append(this_level)
        parent = child
    while depth_stack :
        result.append(depth_stack.pop())
    return result

def depth_order5(root) :
    result = []
    parent = queue()
    parent.append(root)
    while parent :
        child = queue()
        depth_sum = 0
        depth_count = 0
        while parent :
            node = parent.popleft()
            if node :
                depth_sum += node.data
                depth_count += 1
                child.append(node.getLeftChild())
                child.append(node.getRightChild())
        if depth_count: result.append(depth_sum / depth_count)
        parent = child
    return result

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
    print(depth_order5(root))