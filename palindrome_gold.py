import sys

def isPalindrome(s, score) :
    l,r = 0, len(s) - 1
    while(l < r) :
        if(s[l] != s[r]) :
            if(score == 1) : return 1
            else :
                return 1 + min(isPalindrome(s[l + 1: r + 1], 1), isPalindrome(s[l : r], 1))
        else :
            l += 1
            r -= 1
    return 0

def solve() :
    n = int(sys.stdin.readline())
    for _ in range(n) :
        print(isPalindrome(input(), score=0))
    return

if __name__ == '__main__' :
    solve()