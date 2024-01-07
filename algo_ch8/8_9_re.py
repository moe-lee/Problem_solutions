from collections import deque

class MaxQueue(object) :
    def __init__(self) :
        self.main_q_ = deque()
        self.max_q_=  deque()
    
    def enqueue(self, data) :
        self.main_q_.append(data)
        while self.max_q_ and self.max_q_[-1] < data :
            self.max_q_.pop()
        self.max_q_.append(data)
        
    def dequeue(self) :
        if self.main_q_[0] == self.max_q_[0] :
            self.max_q_.popleft();
        return self.main_q_.popleft()

    def max_(self) :
        return self.max_q_[0]

if __name__ =="__main__" :
    q = MaxQueue()
    for i in range(5):
        q.enqueue(i)
    q.enqueue(15)
    for i in range(5, 10) :
        q.enqueue(i)
    print(q.max_q_)
    print(q.max_())