from LinkedList import Forward_list

def reverse_list(l, s, f) :
    ptr = l.head
    for i in range(s-1) : ptr = ptr.next
    rt = ptr.next
    for i in range(f-s) :
        tmp = rt.next
        rt.next = tmp.next
        tmp.next = ptr.next
        ptr.next = tmp
    return l

def reverse_list_whole(l) :
    sublist_head = l.head
    sublist_tail = sublist_head.next
    while sublist_tail.next :
        temp = sublist_tail.next
        sublist_tail.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp
    return l

def reverse_list_step_k(l, k) :
    ptr, n = l.head.next, 0
    while ptr :
        n+=1
        ptr = ptr.next
    n //= k
    sublist_head = l.head
    for i in range(n) :
        sublist_tail = sublist_head.next
        l.print_all()
        for j in range(k-1) :
            tmp = sublist_tail.next
            sublist_tail.next = tmp.next
            tmp.next = sublist_head.next
            sublist_head.next = tmp
        sublist_head = sublist_tail
    return l

if __name__ == "__main__" :
    l = Forward_list([1,2,3,4,5,6,7])
    reverse_list_step_k(l,3).print_all()