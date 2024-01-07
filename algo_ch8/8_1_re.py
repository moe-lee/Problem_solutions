from collections import deque

class DataWithMax(object) :
    def __init__(self, data, max) :
        self.data = data
        self.max_v = max

class stack(object) :
    
    def __init__(self) :
        self.list = deque()

    def push(self, data) :
        if self.list :
            self.list.append(DataWithMax(data, max(data, self.list[-1].max_v)))
        else :
            self.list.append(DataWithMax(data, data))

    
    def pop(self) :
        return self.list.pop()

    def max(self) :
        return self.list[-1].max_v


if __name__ == "__main__" :
    s = stack()
    s.push(22)
    for i in range(10) :
        s.push(i)
    print(s.max())
    s.pop()
    s.pop()
    print(s.max())