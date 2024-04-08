import sys

def solve() :
    N, D, K, C = tuple(map(int, sys.stdin.readline().split()))
    belt = []
    dishes = [0] * (D+1)
    nums = 0
    max_nums = 0
    vonus = 0
    
    for _ in range(N) :
        belt.append(int(sys.stdin.readline()))
    
    for i in range(K) :
        if(not dishes[belt[i]]) : nums += 1
        dishes[belt[i]] += 1
    vonus = 1 if dishes[C] == 0 else 0
    max_nums = nums + vonus
    
    for i in range(K, N + (K - 1)) :
        if(max_nums > K) : break
        dishes[belt[(i - K) % N]] -= 1
        if(dishes[belt[(i - K) % N]] == 0) :
            nums -= 1
        if dishes[belt[i % N]] == 0 :
            nums += 1
        dishes[belt[i % N]] += 1
        
        vonus = 1 if dishes[C] == 0 else 0
        
        max_nums = max(nums + vonus, max_nums)
    
    print(max_nums)
    
    return

if __name__ == '__main__' :
    solve()