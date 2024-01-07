from LinkedList import Forward_list
import time

def even_odd_merge_brute_force(l) :
    odd = Forward_list()
    even = Forward_list()
    ptr = l.head.next
    while ptr is not None :
        if ptr.data % 2 :
            odd.appendNode(ptr)
        else :
            even.appendNode(ptr)
        ptr = ptr.next
    even.extend(odd)
    return even

def even_odd_merge(l) :
    insert_node = l.head
    while insert_node:
        while insert_node.next and insert_node.next.data % 2 == 0:
            insert_node = insert_node.next
        if insert_node.next is None : break
        search_even = insert_node.next
        while search_even.next and search_even.next.data % 2 :
            search_even = search_even.next
        if search_even.next is None : break
        
        
        l.print_all()
        time.sleep(2)
    return l

if __name__ == "__main__" :
    l = Forward_list([1,2,3,4,5,6])
    even_odd_merge(l).print_all()
