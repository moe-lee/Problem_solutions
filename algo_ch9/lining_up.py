import sys
import bisect
def solve() :
    N = int(sys.stdin.readline())
    line = [ int(sys.stdin.readline()) for _ in range(N)]
    longest_sorted_part_length = [1] * (N+1)
    buff = []
    for i in range(len(line)) :
        pos = bisect.bisect_right(buff, line[i])
        if pos >= len(buff) :
            longest_sorted_part_length[i] = len(buff) + 1
            buff.append(line[i])
        else :
            buff[pos] = line[i]
            longest_sorted_part_length[i] = pos + 1
    print(N - max(longest_sorted_part_length))
solve()

'''


'''