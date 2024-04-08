class Node :
    def __init__(self, value = 0, next=None, prev=None) :
        self.value = value
        self.next = next
        self.prev = prev

class BrowerHistory :
    def __init__(self, url) :
        self.curr = Node(value = url)
    
    def visit(self, url) :
        self.curr.next = Node(url, prev=self.curr)
        self.curr = self.curr.next
        return None

    def forward(self, step) :
        while (self.curr.next is not None and  0 < step ) :
            self.curr = self.curr.next
            step -= 1
        return self.curr.value

    def back(self, step) :
        while (self.curr.prev is not None and 0 < step) :
            self.curr = self.curr.prev
            step -= 1
        return self.curr.value

class BrowerHistory2 :
    def __init__(self, url) :
        self.history = [url]
        self.history_cnt = 1
        self.curr_idx = 0
    
    def visit(self, url) :
        self.history.insert(self.curr_idx + 1, url)
        self.history_cnt = self.curr_idx + 2
        self.curr_idx += 1
        return None

    def forward(self, step) :
        self.curr_idx = self.curr_idx + step if(self.curr_idx + step < self.history_cnt) else self.history_cnt - 1
        return self.history[self.curr_idx]

    def back(self, step) :
        self.curr_idx = self.curr_idx - step if(self.curr_idx - step >= 0) else 0
        return self.history[self.curr_idx]