from LinkedList import Forward_list

def even_odd_merge(l) :
    cnt = 1
    iter_ = l.head.next
    odd = Forward_list()
    even = Forward_list()
    while iter_ :
        if cnt & 1 : odd.appendNode(iter_)
        else: even.appendNode(iter_)
        iter_ = iter_.next
        cnt += 1
    even.extend(odd)
    return even

if __name__ == "__main__" :
    l = Forward_list([1,2,3,4,5,6,7,8,9,10])
    even_odd_merge(l).print_all()