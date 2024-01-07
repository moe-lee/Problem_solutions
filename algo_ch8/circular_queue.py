

class Circularqueue(object) :
    def __init__(self, size) :
        self.size = size
        self.list = [0 for i in range(size)]
        self.front = 0
        self.rear = 0
    
    def isFull(self) :
        return (self.rear + 1) % self.size == self.front
    
    def enqueue(self, data) :
        if self.isFull() :
            self.list.insert(self.rear, 0)
            self.size += 1
        self.list[self.rear] = data
        self.rear = (self.rear+1) % self.size
    
    def dequeue(self) :
        if self.rear == self.front : return None
        data = self.list[self.front]
        self.front = (self.front + 1) % self.size
        return data
    
    def getCount(self) :
        return (self.rear - self.front + self.size) % self.size
    
    def print_contents(self):
        idx = self.front
        while idx % self.size != self.rear :
            print(self.list[idx % self.size], end =" ")
            idx+=1
        print()

if __name__ == "__main__" :
    cq = Circularqueue(5)
    for i in range(10) :
        cq.enqueue(i)
    print(cq.list)
    cq.print_contents()