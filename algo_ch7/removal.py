from LinkedList import Forward_list

def remove_node(node) :
    node.data = node.next.data
    node.next = node.next.next

if __name__ == "__main__" :
    l = Forward_list([1,2,3,4,5])
    remove_node(l[2])
    l.node_count -= 1
    l.print_all()