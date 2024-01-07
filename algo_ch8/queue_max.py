from collections import deque as queue

class Queue :
    def __init__(self) :
        self.queue = queue()
        self.data_count = 0
    
    def enqueue(self, data) :
        if self.queue :
            i = len(self.queue) - 1
            while i >= 0 and self.queue[i][0]<data:
                self.queue[i][1], i = data, i-1
        self.queue.append([data, data])
        self.data_count +=1
    
    def dequeue(self) :
        self.data_count -= 1
        return self.queue.popleft()

    def max(self) :
        return self.queue[0][1]


if __name__ == "__main__" :
    q = Queue()
    q.enqueue(10)
    for i in range(10) : q.enqueue(i)
    print(q.max())
    q.dequeue()
    print(q.max())
    q.enqueue(111)
    print(q.max())