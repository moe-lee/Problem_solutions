from collections import deque
'''
def bfs(graph, start_v) :
    queue = deque(start_v)
    visited = [start_v]
    while queue:
        cur_node = queue.popleft()
        for v in graph[cur_node] :
            if v not in visited :
                visited.append(v)
                queue.append(v)
    return visited

graph = []
visited = []

def dfs(cur_v) :
    visited.append(cur_v)
    for v in graph[cur_v] :
        if v not in visited:
            dfs(v)

## for graph
def bfs(graph, start_v) :
    visited = [start_v]
    queue = deque(start_v)
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v] :
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited

# for trees
def bfs(root) :
    if root is None :
        return 0
    q = deque(root)
    visited = []
    while q :
        cur_node = q.popleft()
        visited.append(cur_node)
        if root.left is not None :
            q.append(root.left)
        if root.right is not None :
            q.append(root.right)
    
    return visited

def traversal(root):
    if root is None :
        return None
    traversal(root.left)
    traversal(root.right)
    print(root.value)


def LCA(root, q, p) :
    if root is None :
        return None
    left = LCA(root.left, q, p)
    right = LCA(root.right, q, p)
    if root == q or root == p :
        return root
    elif left and right :
        return root
    return left or right


def maxDeapth(root) :
    max_depth = 0
    if root is None :
        return max_depth
    q = deque((root, 1))
    while q :
        cur_node, cur_depth = q.popleft()
        max_depth = max(max_depth, cur_depth)
        if cur_node.left is not None :
            q.append((cur_node.left, cur_depth + 1))
        if cur_node.right is not None :
            q.append((cur_node.right, cur_depth + 1))
    return max_depth

def maxDepth(root):
    if root is None :
        return 0
    left = maxDeapth(root.left)
    right = maxDeapth(root.right)
    return max(left, right) + 1

def twoSum(nums, target) :
    # python = dynamic list = amotised O(1)
    # deque == linked list
    nums.sort()
    i, j = 0, len(nums) - 1
    while i < j :
        if nums[i] + nums[j] == target :
            return True
        elif nums[i] + nums[j] > target :
            j -= 1
        else :
            i += 1
    return False

def parenthesis(s) :
    stack = []
    for p in s :
        if p == '(' :
            stack.append(')')
        elif p == '{' :
            stack.append('}')
        elif p == '[' :
            stack.append(']')
        else :
            if p != stack.pop():
                return False
    return not stack
'''
def dailyTemperature(temperatures) :
    answer = [0] * len(temperatures)
    stack = []
    for cur_day, cur_temp in enumerate(temperatures) :
        while stack and stack[-1][1] < cur_temp :
            day, _ = stack.pop()
            answer[day] = cur_day
        stack.append((cur_day, cur_temp))
    return answer

def has_two_sum(nums, target) :
    memory = dict()
    for n in nums :
        if (target - n) in memory :
            return True
        memory[nums] = True
    return False

def LongestConsecutiveSequence(nums) :
    memory = dict()
    max_len = 0
    for n in nums :
        memory[n] = n+1
    
    for i in range(len(nums)) :
        if i - 1 not in memory :
            t = i
            while t in memory :
                t = memory[t]
            max_len = max(max_len, t - i)
    
    return max_len

print(dailyTemperature([15, 13, 10, 16, 14, 13, 19, 13, 20, 21]))