class Node :
    def __init__(self, value = 0, next = None) :
        self.value = value
        self.next = next

def append(self, value) :
    new_node = Node(value)
    if not self.head :
        self.head = new_node
    else :
        curr = self.head
        while(curr.next) : curr = curr.next
        curr.next = new_node

class LinkedList :
    def __init__(self) :
        self.head = None
        self.tail = None
    
    def append(self, value) :
        new_node = Node(value)
        if self.head is None :
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = new_node
        
    def insert_at(self, idx, value) :
        new_node = Node(value)
        if idx == 0 :
            new_node.next = self.head
            self.head = new_node
        else :
            current = self.head
            for _ in range(idx - 1) :
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def remove(self, idx) :
        if idx == 0 :
            self.head = self.head.next
        else :
            current = self.head
            for _ in range(idx - 1) :
                current = current.next
            current.next = current.next.next
        
    
    def get(self, idx) :
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value
    

my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

my_list.insert_at(0, 8)
my_list.remove(3)
for i in range(5) :
    print(my_list.get(i))
