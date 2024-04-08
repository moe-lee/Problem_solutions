class ListNode(object) :
    def __init__(self, url, next = None, prev = None) :
        self.url = url
        self.next = next
        self.prev = prev

class BrowserHistory(object) :
    def __init__(self, url) :
        self.curr = ListNode(url)
        print(None)
        return None
    
    def visit(self, url) :
        new_node = ListNode(url, prev=self.curr)
        self.curr.next = new_node
        self.curr = new_node
        print(None)
        return None
    
    def back(self, step) :
        while(step and self.curr.prev) :
            self.curr = self.curr.prev
            step-=1
        print(self.curr.url)
        return self.curr.url
    
    def forward(self, step) :
        while(step and self.curr.next) :
            self.curr = self.curr.next
            step-=1
        print(self.curr.url)
        return self.curr.url

class BrowserHistoryList(object) :
    def __init__(self, url) :
        self.history = [url]
        self.curr_pos = 0
        self.history_bound = 1
        print(None)
        return None
    
    def visit(self, url) :
        self.curr_pos += 1
        if self.curr_pos >= len(self.history) : self.history.append(url)
        else : self.history[self.curr_pos] = url
        self.history_bound = self.curr_pos + 1
        print(None)
        return None
    
    def back(self, step) :
        while(step and self.curr_pos > 0) :
            self.curr_pos -= 1
            step-=1
        print(self.history[self.curr_pos])
        return self.history[self.curr_pos]
    
    def forward(self, step) :
        while(step and self.curr_pos < self.history_bound - 1) :
            self.curr_pos += 1
            step-=1
        print(self.history[self.curr_pos])
        return self.history[self.curr_pos]



if __name__ == '__main__' :
    browserHistory = BrowserHistoryList("leetcode.com")
    browserHistory.visit("google.com")
    browserHistory.visit("facebook.com")
    browserHistory.visit("youtube.com")
    browserHistory.back(1)
    browserHistory.back(1)
    browserHistory.forward(1)
    browserHistory.visit("linkedin.com")
    browserHistory.forward(2)
    browserHistory.back(2)
    browserHistory.back(7)