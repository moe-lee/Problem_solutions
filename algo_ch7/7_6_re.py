from LinkedList import Forward_list
def node_remove(node) :
    node.data = node.next.data
    node.next = node.next.next

if __name__=="__main__" :
    l = Forward_list([1,2,3,4,5,6])
    node_remove(l[4])
    l.node_count-=1
    l.print_all()