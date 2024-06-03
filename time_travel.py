import sys
import copy

def solve() :
    N = int(sys.stdin.readline())
    history = [['t', []]]
    cur_list = []
    for i in range(N) :
        query = list(sys.stdin.readline().split())
        if query[0] != 's' : query[1] = int(query[1])
        history.append(query)
        
        if query[0] == 't' :
            p = query[1] - 1
            while p > 0 and history[p][0] != 't' :
                p -= 1
            cur_list = copy.deepcopy(history[p][1])
            for j in range(p + 1, query[1]) :
                if history[j][0] == 'a' :
                    cur_list.append(history[j][1])
                elif history[j][0] == 's' :
                    if cur_list :
                        cur_list.pop()
            history[-1][1] = copy.deepcopy(cur_list)
            if cur_list : print(cur_list[-1])
            else : print(-1)
        else :
            if query[0] == 'a' :
                cur_list.append(query[1])
            elif query[0] == 's' :
                if cur_list : cur_list.pop()
            if cur_list : print(cur_list[-1])
            else : print(-1)
    return

if __name__ == '__main__' :
    solve()