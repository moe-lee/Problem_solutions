import sys
def solve() :
    T = int(input())
    for _ in range(T) :
        N = int(input())
        U = []
        D = []
        nums = list(map(int, sys.stdin.readline().split()))
        
        possible_flag = True
        
        nums_idx, curr_order = 0, 1
        while nums_idx < N :
            if nums[nums_idx] == curr_order :
                nums_idx += 1
                curr_order += 1
            else:
                if U and U[0] == curr_order :
                    curr_order += len(U)
                    U.clear()
                elif D and D[0] == curr_order :
                    curr_order += len(D)
                    D.clear()
                else :
                    if U and U[-1] == nums[nums_idx] - 1:
                        U.append(nums[nums_idx])
                    elif D and D[-1] == nums[nums_idx] - 1:
                        D.append(nums[nums_idx])
                    else :
                        if not U :
                            U.append(nums[nums_idx])
                        elif not D :
                            D.append(nums[nums_idx])
                        else :
                            possible_flag = False
                            break
                    nums_idx += 1
        print(('YES' if possible_flag else 'NO'))


solve()
