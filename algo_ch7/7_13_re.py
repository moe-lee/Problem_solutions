from LinkedList import Forward_list, ListNode

def list_length(l) :
    ptr, cnt = l.head, 0
    while ptr :
        ptr = ptr.next
        cnt+=1
    return cnt

def add_two_integers(l1, l2) :
    l,s = l1.head.next, l2.head.next
    carry = 0
    res = Forward_list()
    while carry or l or s :
        sum = carry
        if l : 
            sum += l.data
            l = l.next
        if s : 
            sum += s.data
            s = s.next
        carry = sum // 10
        res.appendNode(ListNode(sum % 10))
    return res

if __name__ == "__main__" :
    l1 = Forward_list([3,1,4])
    l2 = Forward_list([7,0,9])
    add_two_integers(l1,l2).print_all()