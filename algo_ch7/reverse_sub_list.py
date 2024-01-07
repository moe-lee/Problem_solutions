# reverse_sub_list.py
from LinkedList import Forward_list

def reverse_sub_list(l, s, f) :
    # check the conditions are vaild
    if s < 0 or s >= l.node_count : return None
    if f < 0 or f < s or f >= l.node_count : return None
    # seperate the sub_list from l
    tmp_head = l[s]
    last_node = l[f]
    l[s-1].next = last_node.next
    last_node.next = None
    
    sub_list = Forward_list(tmp_head)
    sub_list.reverse()
    
    sub_list.tail.next = l[s-1].next
    l[s-1].next = sub_list.head
    
    return l

def reverse_k_unit(l, k):
    for i in range(1, l.node_count, k) :
        l.reverse(i, i+k-1)
    l.print_all()

ll = Forward_list([1,2,3,4])
ll[4].next = ll[2]
print(ll.check_Cycle_ver_1())