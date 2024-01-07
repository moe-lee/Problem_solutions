from LinkedList import Forward_list

def remove_duplicate(l) :
    ptr0, ptr1 = l.head.next, l.head.next
    while ptr0 :
        while ptr1 and ptr1.data == ptr0.data : ptr1 = ptr1.next
        ptr0.next = ptr1
        ptr0 = ptr0.next
    return l

if __name__=="__main__":
    l = Forward_list([1,1,1,2,2,4,4,4,5,6,6,7,7,7,7,7,8,8,8,9])
    remove_duplicate(l)
    Forward_list.print_to_tail_from_head(l)