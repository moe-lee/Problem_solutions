from LinkedList import Forward_list
from LinkedList import ListNode

def get_data(ptr) :
    return ptr.data if ptr else 0

def list_add(l1, l2) :
    res = Forward_list()
    carry,l1_i,l2_i = 0,l1.head.next,l2.head.next
    while carry or l1_i or l2_i :
        sum_ = carry + get_data(l1_i) + get_data(l2_i)
        res.appendNode(ListNode(sum_ % 10))
        carry = sum_ // 10
        if l1_i : l1_i = l1_i.next
        if l2_i : l2_i = l2_i.next
    
    return res

if __name__ == "__main__" :
    l1 = Forward_list([3,1,4])
    l2 = Forward_list([7,0,9])
    res = list_add(l1,l2)
    res.print_all()