import LinkedList

def combine(l, f) :
    r = LinkedList.Forward_list()
    while not(l.isEmpty() or f.isEmpty()) :
        if l[0] < f[0] :
            r.appendNode(l[0])
            l.popLeft()
        else :
            r.appendNode(f[0])
            f.popLeft()
    r.extend(l)
    r.extend(f)
    return r

l = LinkedList.Forward_list([1,3,5,7,9])
f = LinkedList.Forward_list([2,4,6,8,10])
combine(l,f).print_all()
