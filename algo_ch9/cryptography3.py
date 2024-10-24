class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def insert(head, pos, tokens) :
    cur_node = head
    for i in range(pos) :
        cur_node = cur_node.next
    for token in tokens :
        nd = Node(token)
        nd.next = cur_node.next
        cur_node.next = nd
        cur_node = nd

def delete(head, pos, nums) :
    cur_node = head
    for i in range(pos) :
        cur_node = cur_node.next
    end = cur_node
    for i in range(nums + 1) :
        end = end.next
    cur_node.next = end

def append(tail, tokens) :
    for token in tokens :
        nd = Node(token)
        tail.next = nd
        tail = tail.next

for test_case in range(1, 11) :
    N = int(input())
    origin = input().split()
    head = Node('')
    tail = head
    for token in origin :
        nd = Node(token)
        tail.next = nd
        tail = nd
    inst_num = int(input())
    inst = list(input().split())
    idx = 0
    while idx < len(inst) :
        if inst[idx] == 'A' :
            y = int(inst[idx+1])
            tokens = []
            for j in range(0, y) : tokens.append(inst[idx + 2 + j])
            append(tail, tokens)
            idx += 2 + y 
        elif inst[idx] == 'I' :
            x = int(inst[idx+1])
            y = int(inst[idx+2])
            tokens = []
            for j in range(0, y) : tokens.append(inst[idx + 3 + j])
            insert(head, x, tokens)
            idx += 3 + y
        elif inst[idx] == 'D' :
            x = int(inst[idx+1])
            y = int(inst[idx+2])
            delete(head, x, y)
            idx += 3
    print('#'+str(test_case), end="")
    head = head.next
    for i in range(10) :
        if head is None : break
        print(" " + str(head.data), end="")
        head = head.next
    print()

'''
3
10 100 1000
3
I 2 3 1 2 3 D 2 2 A 3 2 5 7
'''