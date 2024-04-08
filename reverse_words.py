def solve() :
    s = input()
    l = 0
    res = ''
    while(l < len(s)) :
        if(s[l] == '<') :
            r = l
            while(s[r] != '>') : r+=1
            r
            res += s[l : r+1]
            l = r
        elif(s[l] != ' ') :
            r = l
            while(r < len(s) and s[r] != ' ' and s[r] != '<') :
                r += 1
            
            for i in range(r-1, l-1, -1) :
                res += s[i]
            l = r - 1
        else :
            res += s[l]
        l += 1
    print(res)


if __name__ == '__main__' :
    solve()