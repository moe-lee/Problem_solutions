import sys

def solve() :
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    length = [0] * len(s2)
    subseq = ['' for _ in range(len(s2))]
    for i in range(len(s1)) :
        prev_max = 0
        cur_sq = ''
        for j in range(len(s2)) :
            tmp_sq = cur_sq
            if prev_max < length[j] :
                cur_sq = subseq[j][:]
            cur_max = max(prev_max, length[j])
            if s1[i] == s2[j] : 
                length[j] = prev_max + 1
                subseq[j] = tmp_sq + s2[j]
            prev_max = cur_max
    print(max(length))
    if max(length) != 0 :
        print(subseq[length.index(max(length))])
solve()