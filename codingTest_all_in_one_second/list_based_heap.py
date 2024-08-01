import heapq

class Heap :
    def __init__(self) :
        self.heap = []
        self.length = 0
        self.compare = lambda x, y : x < y
    
    def getParent(self, idx) :
        return (idx - 1) // 2
    
    def getLeftChild(self, idx) :
        return (idx * 2) + 1
    
    def getRightChild(self, idx) :
        return (idx * 2) + 2
    
    def enqueue(self, data) :
        self.heap.append(data)
        self.length+=1
        newest_ele = self.length - 1
        while newest_ele > 0 and not self.compare(self.heap[self.getParent(newest_ele)], self.heap[newest_ele]) :
            self.heap[self.getParent(newest_ele)], self.heap[newest_ele] = self.heap[newest_ele] , self.heap[self.getParent(newest_ele)]
            newest_ele = self.getParent(newest_ele)
    
    def dequeue(self) :
        if self.length == 0 : return None
        buf = self.heap[0]
        self.length -= 1
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        cur_node = 0
        while self.getLeftChild(cur_node) < self.length :
            suitable_child = self.getLeftChild(cur_node)
            if self.getRightChild(cur_node) < self.length and not self.compare(self.heap[suitable_child], self.heap[self.getRightChild(cur_node)]) :
                suitable_child = self.getRightChild(cur_node)
            
            if self.compare(self.heap[suitable_child], self.heap[cur_node]) :
                self.heap[cur_node], self.heap[suitable_child] = self.heap[suitable_child], self.heap[cur_node]
                cur_node = suitable_child
            else :
                break
        return buf

heap = Heap()
heap.enqueue(99)
heap.enqueue(4)
heap.enqueue(3)
heap.enqueue(2)
heap.enqueue(10)
print(heap.heap)

while heap.heap :
    print(heap.dequeue())

min_heap = [5, 3, 9, 4, 1, 2, 6]
heapq.heapify(min_heap)
