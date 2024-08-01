class Node(object) :
    def __init__(self, value = 0, next = None, prev = None) :
        self.value = value
        self.next = next
        self.prev = prev

class LinkedList(object) :
    def __init__(self) :
        self.head = None
        self.tail = None
    
    def append(self, value) :
        newNode = Node(value=value)
        if self.head is None : 
            self.head = newNode
        else :
            self.tail.next = newNode
        self.tail = newNode
    
    def get(self, idx) :
        if self.head is None :
            return None
        else :
            current = self.head
            while current and idx :
                current = current.next
                idx -= 1
            return current.value if current else None
    
    def insert(self, idx, value) :
        newNode = Node(value=value)
        current = self.head
        for _ in range(idx) :
            current = current.next
        newNode.next = current.next
        current.next = newNode
    def remove(self, idx) :
        if idx  == 0 :
            self.head = self.head.next
        else :
            current = self.head
            for _ in range(idx - 1) :
                current = current.next
            current.next = current.next.next

class BrowserHistory :
    def __init__(self, homepage) :
        self.curr_page = Node(value=homepage)
        print(None)
        return None
    
    def visit(self, url) :
        newPage = Node(value=url)
        self.curr_page.next = newPage
        newPage.prev = self.curr_page
        self.curr_page = self.curr_page.next
        print(None)
        return None
    
    def back(self, steps) :
        while steps and self.curr_page.prev :
            self.curr_page = self.curr_page.prev
            steps -= 1
        print('"'+self.curr_page.value+'"')
    
    def forward(self, steps) :
        while steps and self.curr_page.next :
            self.curr_page = self.curr_page.next
            steps -= 1
        print('"'+self.curr_page.value+'"')


browserHistory = BrowserHistory("leetcode.com")
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