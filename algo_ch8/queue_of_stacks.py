from collections import deque as stack

class queue(object) :
    def __init__(self):
        self.stack1 = stack()
        self.stack2 = stack()
        self.num_of_data = 0
    
    def enqueue(self, data) :
        self.stack1.append(data)
        self.num_of_data+=1
    
    def dequeue(self) :
        if not(self.stack2) :
            if not(self.stack1) : return None
            while self.stack1 :
                self.stack2.append(self.stack1.pop())
        self.num_of_data -= 1
        return self.stack2.pop()

if __name__ == "__main__" :
    q = queue()
    for i in range(10): q.enqueue(i)
    for i in range(10): print(q.dequeue(), end=" ")
    print()
    for i in range(10,30, 3) : q.enqueue(i)
    for i in range(10,30, 3) : print(q.dequeue(), end=" ")