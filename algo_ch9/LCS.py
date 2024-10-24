
def solve() :
    s1 = input()
    s2 = input()
    dp = [0] * len(s2)
    for i in range(0, len(s1)) :
        prev_max = 0
        for j in range(0, len(dp)) :
            cur_max = max(prev_max, dp[j])
            if s1[i] == s2[j] :
                dp[j] = prev_max + 1
            prev_max = cur_max
    print(max(dp))
solve()

'''
KKKXXXABCFFF
ABCKKKRRRFFF

ABCKKKRRRFFF
KKKXXXABCFFF

ABCKKKRRRFFF
ABCRF

ABCRF
ABCKKKRRRFFF

HELLOWORLD
OWOLR


OWOLR
HELLOWORLD
'''