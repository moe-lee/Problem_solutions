from LinkedList import Forward_list

def remove_duplicate(l) :
    ptr1 = l.head.next
    ptr2 = l.head.next
    while ptr1 is not None :
        ptr2 = ptr1.next
        while ptr2 is not None and ptr2.data == ptr1.data : ptr2 = ptr2.next
        ptr1.next = ptr2
        ptr1 = ptr1.next

def remove_duplicate_app(l, m) :
    ptr1 = l.head
    cnt = 1
    while ptr1 is not None :
        ptr2 = ptr1.next
        cnt = 1
        while ptr2 is not None and ptr2.next is not None and ptr2.data == ptr2.next.data :
            ptr2 = ptr2.next
            cnt += 1
        if cnt >= m :
            ptr1.next = ptr2.next
        else:
            ptr1 = ptr2
    return
if __name__ == "__main__" :
    l = Forward_list([1,1,1,2,2,3,4,5,5,5,6,6,7,7,7,7])
    remove_duplicate_app(l, 3)
    head = l.head.next
    while head is not None :
        print(head, end = " ")
        head = head.next