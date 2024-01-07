from LinkedList import Forward_list

def check_palindrome(l) :
    n, ptr0 = 0, l.head
    while ptr0 :
        n += 1
        ptr0 = ptr0.next
    l.reverse(n//2 + 1)
    ptr0, ptr1 = l.head.next, l.head.next
    for i in range(n//2) :
        ptr1 = ptr1.next
    while ptr1:
        if ptr1.data != ptr0.data : 
            l.reverse(n//2 + 1)
            return False
        ptr1,ptr0 = ptr1.next, ptr0.next
    l.reverse(n//2 + 1)
    return True

if __name__ == "__main__" :
    l = Forward_list([1,2,3,4,5,5,4,3,2,1])
    print(check_palindrome(l))
    l.print_all()