from LinkedList import Forward_list

def pivoting(l, k) :
    pivot = Forward_list()
    smaller = Forward_list()
    larger = Forward_list()
    ptr = l.head.next
    while ptr :
        if(ptr.data < k) :
            smaller.appendNode(ptr)
        elif(ptr.data > k) :
            larger.appendNode(ptr)
        else :
            pivot.appendNode(ptr)
        ptr = ptr.next
    res = Forward_list(smaller)
    res.extend(pivot)
    res.extend(larger)
    return res

def pivoting2(l, k) :
    prev_head = None
    pivot_list_head = l.head
    pivot_list_tail = l.head
    tail = l.head   
    while pivot_list_head.data != k:
        if pivot_list_head.next.data == k :
            prev_head = pivot_list_head
        pivot_list_head = pivot_list_head.next
    
    pivot_list_tail = pivot_list_head
    while pivot_list_tail.next and pivot_list_tail.next.data == k :
        pivot_list_tail = pivot_list_tail.next
    if pivot_list_tail.next is None : return
    
    while tail.next : tail = tail.next
    
    tail.next = prev_head.next
    prev_head.next = pivot_list_tail.next
    pivot_list_tail.next = None
    
    iter1 = l.head
    iter2 = pivot_list_tail
    while iter1.next is not pivot_list_head :
        if(iter1.next.data > pivot_list_head.data) :
            iter2.next = iter1.next
            iter1.next = iter1.next.next
            iter2 = iter2.next
        else :
            iter1 = iter1.next
    return l

if __name__ == "__main__" :
    l = Forward_list([1,8,9,10,2,3,4,7,7,7,5,6])
    l = pivoting2(l, 7)
    l.print_all()