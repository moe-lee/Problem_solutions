def twoSum(nums, target) :
    nums.sort()
    l, r = 0, len(nums) - 1
    while(l < r) :
        if(nums[l] + nums[r] == target) :
            return True
        elif (nums[l] + nums[r] > target) :
            r -= 1
        elif (nums[l] + nums[r] < target) :
            l += 1
    return False


class ListNode(object) :
    def __init__(self, value, next = None, prev = None) :
        self.value = value
        self.next = next
        self.prev = prev


class BrowserHistory(object) :
    def __init__(self, root) :
        self.curr = ListNode(root)
        return None
    
    def visit(self, url) :
        self.curr.next = ListNode(url, prev=self.curr)
        self.curr = self.curr.next
        return None
        
    def forward(self, step) :
        while(step and self.curr.next) :
            self.curr = self.curr.next
        return self.curr.value

    def back(self, step) :
        while( step and self.curr.prev) :
            self.curr = self.curr.prev
        return self.curr.value
    
    
if __name__ == '__main__' :
    bh = BrowserHistory('www.leetcode.com')
    print(bh.visit('www.yahoo.co.kr'))
    print(bh.visit('www.google.com'))
    print(bh.visit('www.youtube.com'))
    print(bh.visit('www.naver.com'))
    print(bh.back(2))
    print(bh.forward(1))
    print(bh.back(2))
    print(bh.visit('www.codeit.com'))
    print(bh.back(1))
    print(bh.forward(2))