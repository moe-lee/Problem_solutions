import sys

def solve() :
    T = int(sys.stdin.readline())
    
    def calcParenValue(s, value, sign) :
        highest = 0
        lowest = sys.maxsize
        left_brackets = 0
        for p in range(len(s)) :
            if s[p] == '(' :
                left_brackets += 1
            elif s[p] == ')' :
                left_brackets -= 1
                if s[p-1] == '(' :
                    highest = max(highest, left_brackets)
                    lowest = min(lowest, left_brackets)
                    value[left_brackets] += sign
        return (highest, lowest)
    for _ in range(T) :
        value = [0] * 1500000
        A_max, A_low = calcParenValue(sys.stdin.readline().strip(), value=value, sign=1)
        B_max, B_low = calcParenValue(sys.stdin.readline().strip(), value=value, sign=-1)
        max_rad, low_rad = max(A_max, B_max), min(A_low, B_low)
        
        diff_idx = -1
        i = low_rad
        while i <= max_rad :
            if value[i] != 0 :
                if diff_idx >= 0 :
                    if i - diff_idx < 19 :
                        value[i] += (value[diff_idx]/(2 ** (i - diff_idx)))
                diff_idx = i
            i += 1
        if value[diff_idx] < 0 : print('<')
        elif value[diff_idx] > 0 : print('>')
        else : print('=')
solve()