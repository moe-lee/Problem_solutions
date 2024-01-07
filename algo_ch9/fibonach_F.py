import copy

zero_tbl = [1, 0]
one_tbl = [0, 1]

for i in range(2, 41) :
    zero_tbl.append(zero_tbl[i-1] + zero_tbl[i-2])
    one_tbl.append(one_tbl[i-1] + one_tbl[i-2])

def fibonacci_count(n) :
    print(zero_tbl[n], one_tbl[n])

def solve() :
    t = int(input())
    for i in range(t) :
        n = int(input())
        fibonacci_count(n)


def main() :
    solve()

main()