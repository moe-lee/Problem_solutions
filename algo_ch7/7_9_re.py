from LinkedList import Forward_list

def right_rotate(l, k) :
    if k == 0 : return l
    tail = l.head
    n = 0
    while tail.next :
        tail = tail.next
        n += 1
    tail.next = l.head.next
    n -= (k % n)
    for i in range(n) :
        tail = tail.next
    l.head.next = tail.next
    tail.next = None
    return l


if __name__ == "__main__" :
    l = Forward_list([1,2,3,4,5,6,7])
    right_rotate(l,3).print_all()