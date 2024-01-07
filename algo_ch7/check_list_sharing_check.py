from LinkedList import Forward_list

def list_share_check(l1, l2) :
    l1_tail = l1.head
    l2_tail = l2.head
    while not l1_tail.isTail() : l1_tail = l1_tail.next
    while not l2_tail.isTail() : l2_tail = l2_tail.next
    return l1_tail is l2_tail

def get_Tail(list, *target) :
    ptr = list.head
    #print(target)
    
    while ptr.next not in target and ptr.next is not None:
        ptr = ptr.next
    return ptr

def find_first_shared_node(l1, l2 ):
    common_tail = get_Tail(l1)
    while not common_tail.isTail() : common_tail = common_tail.next
    tan_lists = [l1, l2]
    cross_ptr = [l1.head, l2.head]
    ptr_idx = 0
    while cross_ptr[0].next is not common_tail : cross_ptr[0] = cross_ptr[0].next
    while cross_ptr[1].next is not common_tail and cross_ptr[1].next is not cross_ptr[0] : cross_ptr[1] = cross_ptr[1].next
    print("outer", cross_ptr)
    
    while all(cross_ptr[i] is not tan_lists[i].head for i in range(2)):
        common_tail = cross_ptr[ptr_idx % 2]
        cross_ptr[ptr_idx % 2] = tan_lists[ptr_idx % 2].head.next
        while cross_ptr[ptr_idx % 2].next is not common_tail and cross_ptr[ptr_idx % 2].next is not cross_ptr[(ptr_idx+1) % 2] :
            cross_ptr[ptr_idx % 2] = cross_ptr[ptr_idx % 2].next
        print(common_tail, cross_ptr)
        if(cross_ptr[ptr_idx % 2].next is common_tail) : break
        ptr_idx += 1
    
    return common_tail

def find_first_shared_node_ver2(l1, l2) :
    l1_length = 0
    l2_length = 0
    tmp_ptr = l1.head
    while tmp_ptr is not None : 
        l1_length += 1
        tmp_ptr = tmp_ptr.next
    tmp_ptr = l2.head
    while tmp_ptr is not None :
        l2_length += 1
        tmp_ptr = tmp_ptr.next
    long_len = max(l1_length, l2_length)
    shrt_len = min(l1_length, l2_length)
    short, long = (l1.head, l2.head) if l1_length < l2_length else (l2.head,l1.head)
    for i in range(long_len - shrt_len) :
        long = long.next
    while long.next is not short.next and long.next is not None:
        long = long.next
        short = short.next
    return long.next

l1 =Forward_list([1])
l2 =Forward_list([1,2,3,4,5,6])
l1.tail.next = l2[4]

print(find_first_shared_node_ver2(l1, l2))