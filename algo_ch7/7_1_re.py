from LinkedList import Forward_list
from LinkedList import LinkedList

def merge_sorted_lists(l1, l2) :
    res = Forward_list()
    while l1.head.next and l2.head.next :
        res.appendNode((l1.popLeft()) if l1.head.next.data < l2.head.next.data else l2.popLeft())
    res.extend(l1)
    res.extend(l2)
    return res

if __name__ == "__main__" :
    l1 = Forward_list([1,2,3,7,9,15,17])
    l2 = Forward_list([4,5,6,8,13,19])
    merge_sorted_lists(l1,l2).print_all()