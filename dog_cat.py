def solve() :
    N = int(input())
    S = input()
    look_up_table = {}
    l, r = 0, 0
    max_len, sub_len = 0, 0
    while( r <= len(S) ) :
        if r == len(S):
            max_len = max(max_len, r - l)
            break
        if len(look_up_table) < N or S[r] in look_up_table:
            look_up_table[S[r]] = (1 if S[r] not in look_up_table else look_up_table[S[r]] + 1)
            r += 1
        else :
            max_len = max(max_len, r - l)
            if look_up_table[S[l]] == 1 : look_up_table.pop(S[l])
            else : look_up_table[S[l]] -= 1
            l += 1
    print(max_len)
    return

if __name__ == '__main__' :
    solve()