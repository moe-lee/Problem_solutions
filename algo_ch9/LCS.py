import sys

def solve() :
    s1 = sys.stdin.readline().strip('\n')
    s2 = sys.stdin.readline().strip('\n')
    sc_tbl = [0] * 1000
    for i in range(len(s1)) :
        j = len(s2) - 1
        while j >= 0 : 
            if s2[j] == s1[i] :
                k = j - 1
                # 같은 문자로 이전 인덱스에 증가시킨 값을 이용하지 않기 위해 끝에서부터 처리한다.
                while k >= 0 and sc_tbl[k] == 0 : k-=1
                sc_tbl[j] = max(sc_tbl[j], 1 + (0 if k < 0 else sc_tbl[k]))
            j -= 1
    print(max(sc_tbl))

if __name__ == "__main__" :
    solve()