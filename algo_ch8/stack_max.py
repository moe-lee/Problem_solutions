from LinkedList import ListNode
import collections

class StackDataWithMax(object) :
    def __init__(self, data, max_) :
        self.data = data
        self.max = max_
    
class Stack :
    def __init__(self) :
        self.top = ListNode(StackDataWithMax(None, -9999))
        self.count = 0
        
    def push(self, *items) :
        for i in items :
            if self.top.next is None :
                new_node = ListNode(StackDataWithMax(i, i))
            else :
                new_node = ListNode(StackDataWithMax(i, max(i,self.top.next.data.max)))
            new_node.next = self.top.next
            self.top.next = new_node
            self.count += 1
    
    def pop(self) :
        item = self.top.next
        self.top.next = self.top.next.next
        self.count -= 1
        return item.data
    
    def top(self) :
        return self.top.next
    
    def empty(self) :
        return self.top.next is None
    
    def max(self) :
        return self.top.next.data.max

if __name__ == "__main__" :
    s = Stack()
    s.push(1,2,9,4,9)
    print(s.max())
    s.pop()
    print(s.max())
    s.pop()
    print(s.max())
    s.pop()
    print(s.max())