from LinkedList import Forward_list

def get_k_end_node(l, k) :
    ptr, tail = l.head,l.head
    for i in range(k) : tail = tail.next
    while tail: ptr, tail = ptr.next, tail.next
    return ptr

if __name__ == "__main__" :
    l = Forward_list([1,2,3,4,5,6])
    print(get_k_end_node(l,4))