from LinkedList import Forward_list

def check_cycle(l1) :
    maps = dict()
    ptr = l1.head
    while ptr and maps.get(id(ptr),True) :
        maps[id(ptr)] = False
        ptr = ptr.next
    return ptr

def check_cycle2(l) :
    fast, slow = l.head, l.head
    
    while fast is l.head or fast and fast.next and fast.next.next and fast is not slow :
        fast = fast.next.next
        slow = slow.next
    if fast is None : return None
    
    fast = fast.next
    k = 0
    
    while fast is not slow :
        fast = fast.next
        k += 1
    slow = l.head
    fast = slow
    for i in range(k+1) :
        fast = fast.next
    while slow is not fast :
        slow = slow.next
        fast = fast.next
    return slow

if __name__ == "__main__" :
    l = Forward_list([1,2,3,4,5,6,7,8,9])
    l[9].next = l[2]
    print(check_cycle2(l))