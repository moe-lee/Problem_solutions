from collections import deque

class circular_queue(object) :
    def __init__(self, size) :
        self.list = deque()
        for i in range(size) : self.list.append(None)
        self.count = 0
        self.front = 0
        self.rear = 0
        self.size = size
        self.size_factor = size-1
        
    def enqueue(self, data) :
        if self.count == self.size - 1 :
            self.list.rotate(-(self.front))
            self.list.extend(deque([None] * self.size_factor))
            self.front = 0
            self.rear = self.count
            self.size += self.size_factor
        
        self.list[self.rear] = data
        self.count += 1
        self.rear = (self.rear + 1) % self.size
    
    def dequeue(self) :
        if self.front == self.rear : return None
        
        data = self.list[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return data
    
    def getNumberOfData(self) :
        return self.count
    
if __name__ == "__main__" :
    q = circular_queue(5)
    print(q.list)
    for i in range(10) :
        q.enqueue(i)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    print(q.list, q.front, q.rear, q.size)
    for i in range(111,117) :
        q.enqueue(i)
    print(q.list)
    head = q.front
    while (head % q.size) != q.rear :
        print(q.list[head % q.size], end=" ")
        head+=1