from collections import deque as stack

class DatawithMax(object) :
    def __init__(self, data, max_) :
        self.data = data
        self.max_ = max_
    def __repr__(self) :
        return str(self.data)+", "+str(self.max_)
    
class Queue(object) :
    def __init__(self) :
        self.e_stack_ = stack()
        self.d_stack_ = stack()
        self.num_of_data = 0
    
    def enqueue(self, data) :
        max_v = data
        if self.e_stack_ :
            max_v = max(max_v, self.e_stack_[-1].max_)
        elif self.d_stack_ :
            max_v = max(max_v, self.d_stack_[0].max_)
        self.e_stack_.append(DatawithMax(data, max_v))
        self.num_of_data += 1
    
    def dequeue(self) :
        if not self.d_stack_ :
            while self.e_stack_ :
                self.d_stack_.append(self.e_stack_.pop())
        return self.d_stack_.pop()
    
    def max(self) :
        if self.e_stack_:
            return self.e_stack_[-1].max_v
        elif self.d_stack_ :
            return self.d_stack_[0].max_v
        return None

if __name__ =="__main__" :
    q = Queue()
    for i in range(10) :
        q.enqueue(i)
    q.enqueue(20)
    for i in range(10, 20) :
        q.enqueue()