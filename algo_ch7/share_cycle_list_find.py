from LinkedList import Forward_list

def check_share_brute_force(l1, l2) :
    l1_nodes = dict()
    ptr1 = l1.head.next
    while l1_nodes.get(ptr1, True) :
        l1_nodes[ptr1] = False
        ptr1 = ptr1.next
    ptr1 = l2.head
    while l1_nodes.get(ptr1, True) :
        ptr1 = ptr1.next
    return ptr1

def get_cycle_cnt(list) :
    ptr = list.head
    k_cnt = 1
    ptr_old = None
    while ptr is not None and ptr_old is not ptr:
        ptr_old = ptr
        for j in range(k_cnt) : 
            if(ptr is None) : return 0
            ptr = ptr.next
        k_cnt += 1
    return k_cnt if ptr else 0

def get_length(list, end) :
    cnt = 0
    while list is not end and list is not None:
        list = list.next
        cnt += 1
    return cnt if list else 0

def get_first_node_shared(l1, l2, end) :
    l1_len = get_length(l1.head, end)
    l2_len = get_length(l2.head, end)
    # 둘의 테일이 다른 경우 -> 공유하지 않는다.
    if not (l1_len * l2_len) : return None

    long, short = (l1.head, l2.head) if l1_len > l2_len else (l2.head, l1.head)
    for i in range(abs(l1_len - l2_len)) : long = long.next
    while long is not short :
        long = long.next
        short = short.next
    return long

def check_share(l1, l2) :
    # 사이클여부와 노드 개수 구하기
    l1_cycle_node_number = get_cycle_cnt(l1)
    l2_cycle_node_number = get_cycle_cnt(l2)
    print(l1_cycle_node_number, l2_cycle_node_number)
    # 어느 한 쪽만 사이클이 있는 경우
    if (not l1_cycle_node_number and l2_cycle_node_number) or (l2_cycle_node_number and not l1_cycle_node_number) :
        return None
    # 둘 다 사이클이 없는 경우
    if not(l1_cycle_node_number or l2_cycle_node_number) :
        tail = l1.head
        while not tail.isTail() : tail = tail.next
        return get_first_node_shared(l1, l2, tail)
    #둘 다 사이클이 있는 경우
    # 사이클 노드 개수가 다르면 공유하지 않는다.
    if l1_cycle_node_number != l2_cycle_node_number : return None
    
    # 사이클이 둘다 존재할 경우, 둘의 사이클 시작 노드를 구한다.
    # 사이클 시작 위치 구하기
    cycle_head = [l1.head, l2.head]
    for i in range(2) :
        cycle_head_fast = cycle_head[i]
        for j in range(l1_cycle_node_number - 1) : cycle_head_fast = cycle_head_fast.next
        while cycle_head[i] is not cycle_head_fast : 
            cycle_head_fast = cycle_head_fast.next
            cycle_head[i] = cycle_head[i].next
    print(cycle_head)
    
    #두 위치를 비교한다. 같은 곳에서 사이클이 시작하면, 사이클 시작 노드 이전에 공유노드가 있다.
    if cycle_head[0] is cycle_head[1] :
        shared_node = get_first_node_shared(l1,l2, cycle_head[0])
        return shared_node
    else :
        # 사이클 시작 위치가 다르면 2가지 가능성이 있다. 1. 서로 다른 리스트 2. 서로 같은 리스트
        cycle_head_l2 = cycle_head[1]
        for i in range(l1_cycle_node_number) :
            if cycle_head_l2 is cycle_head[0] :
                return cycle_head[0]
        return None


l1 = Forward_list([1,2,3,4])
l2 = Forward_list(['a','b','c','d'])
print(check_share(l1, l2))