# Linked list api.
import time

class ListNode :
    def __init__(self, data, next = None) :
        self.data = data
        self.next = next
    
    def isTail(self) :
        return not(self.next)
    
    def __repr__(self) :
        return str(self.data)
    
    def __str__(self) :
        return str(self.data)
    
    def __lt__(self, cmp) :
        return self.data < cmp.data
    
    def __gt__(self, cmp) :
        return self.data > cmp.data
    
    def __le__(self, cmp) :
        return self.data <= cmp.data
    
    def __ge__(self, cmp) :
        return self.data >= cmp.data
    
    def __eq__(self, cmp) :
        return self is cmp
    
    def __ne__(self, cmp) :
        return self.data != cmp.data

class List(object) :
    def __init__(self) :
        pass

    def appendNode(self, node) :
        pass
    
    def appendNodeLeft(self, node) :
        pass
    
    def insert(self, node, k) :
        pass
    
    def remove(self, node) :
        pass
    
    def search(self, node) :
        pass
    
    def pop(self) :
        pass
    
    def popLeft(self) :
        pass
    
    def extends(self, list) :
        pass
    
class Forward_list(List):
    def __init__(self, initial_object = None) :
        super().__init__()
        self.head = ListNode(None,None) # dummy node
        self.node_count = 0
        self.tail = self.head
        insert_ptr = self.head
        
        if isinstance(initial_object, Forward_list) :
            self.head = initial_object.head
            self.tail = initial_object.tail
            self.node_count = initial_object.node_count
        
        elif isinstance(initial_object, ListNode) :
            self.head.next = initial_object
            self.node_count+=1
            self.tail = self.head
            while not self.tail.isTail() :
                self.tail = self.tail.next
                self.node_count+=1
            
        elif hasattr(initial_object, "__iter__") :
            for i in initial_object :
                insert_ptr.next = ListNode(i, None)
                insert_ptr = insert_ptr.next
                self.tail = insert_ptr
            self.node_count += len(initial_object)
    
    @staticmethod
    def print_to_tail_from_head(l) :
        ptr = l.head.next
        print("[ ", end="")
        while ptr :
            print(ptr, end=" ")
            ptr = ptr.next
        print("]")
    
    def isEmpty(self) :
        return self.head.next is None
    
    def appendNode(self, node) :
        if not isinstance(node, ListNode) :
            raise ValueError
        self.tail.next = node
        self.tail = self.tail.next
        self.node_count+=1
    
    def appendNodeLeft(self, node) :
        if not isinstance(node, ListNode) :
            raise ValueError
        node.next = self.head.next
        self.head.next = node
        self.node_count +=1
    
    def search(self, key) :
        ptr = self.head
        while ptr and ptr.data != key :
            ptr = ptr.next
        return ptr
    
    def remove(self, node) :
        if node.isTail() : return
        ptr = self.head
        while ptr and ptr.next is not node :
            ptr = ptr.next
        ptr.next = node.next
        self.node_count-=1
        return ptr
    
    def pop(self) :
        if self.isEmpty() : raise IndexError
        
        ptr = self.head.next
        while not ptr.next.isTail() :
            ptr = ptr.next
        self.tail = ptr
        ptr = self.tail.next
        self.tail.next = None
        self.node_count -= 1
        return ptr
    
    def popLeft(self) :
        if self.isEmpty() : raise IndexError
        
        ptr = self.head.next
        self.head.next = self.head.next.next
        self.node_count -= 1
        return ptr
    
    def __getitem__(self, index) :
        cnt = 0
        ptr = self.head
        while cnt < index : 
            ptr = ptr.next
            cnt +=1
        return ptr
    
    def insert(self, node, k) :
        if k > self.node_count : return None
        
        cur = 0
        insert_pos = self.head
        while cur < k :
            insert_pos = insert_pos.next
            cur += 1
        node.next = insert_pos.next
        insert_pos.next = node
        self.node_count+=1
        return node
    
    def reverse(self, s = 1, f = 0) :
        if f <= s : f = self.node_count
        prior = self[s-1]
        cur = self[s]
        for i in range(f - s) :
            tmp1 = cur.next
            cur.next = tmp1.next
            tmp2 = prior.next
            prior.next = tmp1
            tmp1.next = tmp2
        
        return self

    def print_all(self) :
        print("[", end="")
        for i in range(1, self.node_count + 1) :
            print(self[i], end = " ")
        print("]")

    def extend(self, list) :
        if list and (not list.isEmpty()) :
            self.tail.next = list.head.next
            self.tail = list.tail
            self.node_count += list.node_count
    
    # spend O(n) spaces.
    def check_Cycle_without_node_count_ver_1(self) :
        visit_tbl = dict()
        ptr = self.head.next
        while visit_tbl.get(id(ptr), 0) < 2 : # when some sequence type be applyed, it's expected to spend O(n) time complexity when search.
            # map would be used instead of array. it requires short running time at least O(1).
            visit_tbl[id(ptr)] = visit_tbl.get(id(ptr), 0) + 1
            ptr = ptr.next
        return ptr
    
    # cut the links in traversal, and find null pointer
    def check_Cycle_without_node_count_ver_2(self) :
        cycle_iter1 = self.head
        cycle_iter2 = self.head.next
        while not cycle_iter2.isTail():
            cycle_iter1 = cycle_iter2
            cycle_iter2 = cycle_iter2.next
            cycle_iter1.next = None
        return cycle_iter2
    
    def check_Cycle_without_node_count_ver_3(self) :
        iter_head_1 = self.head
        iter_head_2 = self.head.next
        while iter_head_1 is not iter_head_2 and iter_head_2 is not None :
            iter_head_2 = iter_head_2.next
            iter_head_2 = iter_head_2.next
            iter_head_1 = iter_head_1.next
        print(iter_head_1, iter_head_2)

    def check_Cycle_without_node_count_ver_4(self) :
        iter1_head = self.head
        iter2_head = self.head
        iter2_cnt = 0
        while iter1_head is not None :
            iter1_head = iter1_head.next
            iter2_head = self.head
            tmp_cnt = 0
            while iter2_head != iter1_head :
                iter2_head = iter2_head.next
                tmp_cnt += 1
            if tmp_cnt < iter2_cnt :
                break
            iter2_cnt = tmp_cnt
        return iter1_head
    
    def check_Cycle_without_node_count_ver5(self) :
        end_point = self.head.next
        start_point = self.head
        max_step_cnt = 0
        start_to_end = 0
        while end_point is not None :
            start_point = self.head
            start_to_end = 0
            while start_point is not end_point :
                start_point = start_point.next
                start_to_end += 1
            if start_to_end < max_step_cnt :
                break
            else :
                max_step_cnt = start_to_end
            end_point = end_point.next
        return end_point
        
    def check_cycle_list_two_path(self) :
        k_ch = 1
        iter_1 = self.head.next
        iter_1_before = self.head
        while iter_1 is not None and iter_1_before != iter_1:
            iter_1_before = iter_1
            j = 0
            while j < k_ch and iter_1 is not None :
                iter_1 = iter_1.next
                j+=1
            k_ch+=1
        if iter_1 :
            iter_1 = self.head.next
            iter_2 = iter_1
            for i in range(k_ch - 1) : iter_2 = iter_2.next
            while iter_1 is not iter_2 :
                time.sleep(1)
                iter_1 = iter_1.next
                iter_2 = iter_2.next
        return iter_1
    

class Node(ListNode) :
    def __init__(self, data, prev=None, next=None):
        super().__init__(data, next)
        self.prev = prev

class LinkedList(List) :
    def __init__(self, iterable_object = None) :
        super().__init__()
        self.head = Node(None, None, None)
        self.tail = self.head
        self.node_cnt = 0
        
        if isinstance(iterable_object, LinkedList) :
            self.head = LinkedList.head
            self.tail = LinkedList.tail
            self.node_cnt = LinkedList.node_cnt
        elif isinstance(iterable_object, Node) :
            self.tail.next = Node
            Node.prev = self.tail
            while self.tail.next : 
                self.tail = self.tail.next
                self.node_cnt += 1
        elif hasattr(iterable_object, "__iter__"):
            ptr = self.head
            for item in iterable_object :
                new_node = Node(item, None, None)
                ptr.next, new_node.prev = new_node, ptr
                ptr = ptr.next
                self.tail = ptr
            self.node_cnt += len(iterable_object)
    
    @staticmethod
    def check_node_type(node) :
        if not isinstance(node, Node) :
            raise ValueError
    
    def appendNode(self, node):
        LinkedList.check_node_type(node)
        self.tail.next= node
        node.prev = self.tail
        self.tail = self.tail.next
        self.node_cnt += 1
    
    def appendNodeLeft(self, node):
        LinkedList.check_node_type(node)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.node_cnt += 1
    
    def insert(self, node, k):
        LinkedList.check_node_type(node)
        if k > self.node_cnt :
            raise IndexError
        
        ptr = self.head
        for i in range(k) :
            ptr = ptr.next
        node.next = ptr.next
        node.prev = ptr
        ptr.next.prev = node
        ptr.next = node
        self.node_cnt += 1
        if(self.tail.next) :
            self.tail = self.tail.next
    
    def remove(self, node) :
        if node is self.tail :
            return
        
        node.prev.next = node.next
        node.next.prev = node.prev
        self.node_cnt -= 1
    
    def pop(self) :
        if self.node_cnt < 1 : return
        ptr = self.tail
        self.tail = self.tail.prev
        self.tail.next.prev = None
        self.tail.next = None
        self.node_cnt -= 1
        return ptr
    
    def popLeft(self):
        if self.node_cnt < 1 : return
        ptr = self.head.next
        ptr.next.prev = self.head
        ptr.prev.next = ptr.next
        self.node_cnt -= 1
        return ptr
    
    def search(self, node):
        ptr = self.head
        while ptr and node != ptr.data :
            ptr = ptr.next
        return ptr
    
    def __getitem__(self, index) :
        ptr = self.head
        for i in range(index) : ptr = ptr.next
        return ptr
    
    def print_all(self) :
        ptr = self.head.next
        print("[ ",end="")
        while ptr :
            print(ptr,end=" ")
            ptr = ptr.next
        print("]")
    
if __name__ == "__main__" :
    mylist = LinkedList([1,2,3,4])
    mylist.print_all()
    mylist.remove(mylist[3])
    mylist.print_all()
    mylist.appendNode(Node(3))
    mylist.print_all()
    mylist.pop()
    mylist.popLeft()
    mylist.print_all()
    mylist.insert(Node(3), 1)
    mylist.print_all()
    print(mylist.search(5))
    