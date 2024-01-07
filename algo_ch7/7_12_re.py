from LinkedList import Forward_list

def pivoting(l, key) :
    equals = Forward_list()
    largers = Forward_list()
    smallers = Forward_list()
    ptr = l.head.next
    while ptr :
        if ptr.data > key :
            largers.appendNode(ptr)
        elif ptr.data < key :
            smallers.appendNode(ptr)
        else :
            equals.appendNode(ptr)
        ptr = ptr.next
    smallers.extend(equals)
    smallers.extend(largers)
    return smallers

if __name__ == "__main__" :
    l = Forward_list([1,9,2,5,3,2,6,4,5,7,4,2,3,7,8,5,4,6,4])
    pivoting(l, 4).print_all()