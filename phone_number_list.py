import sys
class TreeNode :
    def __init__(self, number, left=None, right= None):
        self.number = number
        self.child = [None] * 10
        self.childCnt = 0


def solve() :
    root = TreeNode(-1)
    phone_numbers = []
    n = int(sys.stdin.readline())
    for _ in range(n) :
        phone_numbers.append(sys.stdin.readline().strip())
    
    for num in phone_numbers :
        cur_node = root
        i = 0
        while i < len(num) and cur_node.child[ord(num[i]) - 0x30] :
            cur_node = cur_node.child[ord(num[i]) - 0x30]
            if(cur_node.childCnt == 0) :
                print('NO')
                return
            i += 1
        
        if  i == len(num) :
            print('NO')
            return
        
        while i < len(num) :
            cur_node.child[(ord(num[i]) - 0x30)] = TreeNode(ord(num[i]) - 0x30)
            cur_node.childCnt += 1
            cur_node = cur_node.child[ord(num[i]) - 0x30]
            i+=1
    print('YES')

t = int(input())
for _ in range(t) :
    solve()