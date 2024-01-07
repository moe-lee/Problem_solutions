from LinkedList import Forward_list

def check_shared_list(l1,l2) :
    ptr_1, ptr_2 = l1.head, l2.head
    while ptr_1.next or ptr_2.next :
        if ptr_1.next : ptr_1 = ptr_1.next
        if ptr_2.next : ptr_2 = ptr_2.next
    return ptr_1 is ptr_2

def getListLength(l1) :
    ptr = l1.head
    count = 0
    while ptr :
        ptr = ptr.next
        count += 1
    return count

def check_and_get_shared_node(l1, l2) :
    l1_count, l2_count = getListLength(l1), getListLength(l2)
    diff = l1_count - l2_count
    ptr_1, ptr_2 = l1.head, l2.head
    
    if diff < 0 : 
        for i in range(abs(diff)) : ptr_2 = ptr_2.next
    else : 
        for i in range(diff) : ptr_1 = ptr_1.next
    
    while ptr_1 and ptr_2 and ptr_1 is not ptr_2 :
        ptr_1, ptr_2 = ptr_1.next, ptr_2.next
    return ptr_1

if __name__ == "__main__" :
    l1 = Forward_list([1,2,3,4,5,6,7,8,9])
    l2 = Forward_list([1,2,3])
    l2[3].next = l1[6]
    print(check_and_get_shared_node(l1,l2))