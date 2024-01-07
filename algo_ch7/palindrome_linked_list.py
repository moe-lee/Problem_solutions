from LinkedList import Forward_list
from LinkedList import LinkedList
import collections

def check_palindrome_brute_force(l) :
    ptr_last = l.head.next
    while ptr_last.next : ptr_last = ptr_last.next
    
    ptr_front = l.head.next
    while ptr_front is not ptr_last :
        if(ptr_front.data != ptr_last.data) : return False
        ptr_front = ptr_front.next
        tptr = ptr_front
        while tptr is not ptr_last and tptr.next is not ptr_last :
            tptr = tptr.next
        ptr_last = tptr
    return True

def check_palindrome2(l) :
    n = 0
    ptr = l.head.next
    while ptr :
        n += 1
        ptr = ptr.next
    l.reverse(n // 2 + 1)
    l.print_all()
    ptr1 = l.head
    ptr2 = l.head
    for i in range(n//2) :
        ptr2 = ptr2.next
    for i in range(n//2) :
        ptr1 = ptr1.next
        ptr2 = ptr2.next
        if(ptr1.data != ptr2.data) : 
            l.reverse(n//2 + 1)
            return False
    l.reverse(n//2 + 1)
    return True

def check_palindrome3(list_) :
    list_.print_all()
    head = list_.head.next
    tail = list_.tail
    while head is not tail and tail.next is not head :
        if head.data != tail.data : return False
        head = head.next
        tail = tail.prev
    return True

if __name__ == "__main__" :
    l = Forward_list(['a','b','c','c','b','a'])
    print(check_palindrome2(l))
    l2 = LinkedList(['a','b','c','t','b','a'])
    print(check_palindrome3(l2))