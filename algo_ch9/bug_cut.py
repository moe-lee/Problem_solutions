import sys

def solve() :
    N = int(sys.stdin.readline())
    bug = list(map(int, sys.stdin.readline().split()))
    X, Y = 0, N-1
    thorax = sum(bug[1:N-1])
    abdomen = bug[Y]
    head = bug[X]
    num_of_pairs = 0
    while X >= 0 and X < Y:
        if thorax <= abdomen :
            thorax += bug[X]
            head -= bug[X]
            X -= 1
        elif head + bug[X+1] < abdomen and thorax - bug[X+1] > abdomen :
            X += 1
            head += bug[X]
            thorax -= bug[X]
        else:
            if abdomen > head :
                num_of_pairs += X+1
            Y -= 1
            abdomen += bug[Y]
            thorax -= bug[Y]
    print(num_of_pairs)

solve()