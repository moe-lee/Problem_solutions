from LinkedList import Forward_list
import collections

def reverse_order(l) :
    stack = collections.deque()
    ptr = l.head.next
    while ptr :
        stack.append(ptr)
        ptr = ptr.next
    
    while stack :
        node = stack.pop()
        print(node, end=" ")
    return

if __name__ == "__main__" :
    l = Forward_list([1,2,3,4,5,6,7])
    reverse_order(l)