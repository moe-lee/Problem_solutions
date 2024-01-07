from LinkedList import Forward_list

def remove_node(node) :
    node.data = node.next.data
    node.next = node.next.next

def k_th_node_remove(l, k) :
    ptr1 = l.head
    ptr2 = l.head
    for i in range(k) : ptr2 = ptr2.next
    while ptr2 is not None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next        
    remove_node(ptr1)
    return

if __name__ == "__main__" :
    l = Forward_list([1,2,3,4,5])
    k_th_node_remove(l, 2)
    l.node_count -= 1
    l.print_all()