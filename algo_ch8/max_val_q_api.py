import collections

class Maxqueue(object) :
    def __init__(self) :
        self.list = collections.deque()
        self.max_q = collections.deque()
    
    def enqueue(self, data) :
        while self.max_q and self.max_q[-1] < data : self.max_q.pop()
        self.max_q.append(data)
        self.list.append(data)
    
    def dequeue(self) :
        if self.list[0] == self.max_q[0] :
            self.max_q.popleft()
        return self.list.popleft()
    
    def max(self) :
        return self.max_q[0]

if __name__=="__main__" :
    q = Maxqueue()
    q.enqueue(3)
    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(2)
    q.enqueue(0)
    print(q.list)
    print(q.max_q)
    q.enqueue(1)
    print(q.list)
    print(q.max_q)
    q.dequeue()
    print(q.list)
    print(q.max_q)
    q.dequeue()
    print(q.list)
    print(q.max_q)
    q.enqueue(2)
    print(q.list)
    print(q.max_q)
    q.enqueue(4)
    print(q.list)
    print(q.max_q)
    q.enqueue(4)
    print(q.list)
    print(q.max_q)
    q.enqueue(4)
    print(q.list)
    print(q.max_q)
    q.enqueue(4)
    print(q.list)
    print(q.max_q)
    q.enqueue(4)
    print(q.list)
    print(q.max_q)
    