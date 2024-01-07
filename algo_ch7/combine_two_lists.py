# combine_two_lists.py
from collections import deque

# 단순 연결리스트 - 오직 next 로만 연결된 Linked List.
def combine_two_chain_brute_force(l, f) :
    result = deque()
    # 양쪽 리스트의 헤드를 검사해 더 작은 쪽을 결과 리스트에 추가한다.
    while len(l) * len(f) != 0 :
        if(l[0] < f[0]) :
            result.append(l[0])
            l.popleft()
        else :
            result.append(f[0])
            f.popleft()
    # 남은 노드들을 모두 result에 연결한다.
    result.extend(l)
    result.extend(f)
    return result

def combine_two_chain(l,f) :
    i = 0
    # 리스트 f가 빌 떄까지, f의 노드를 l에 삽입한다.
    while f :
        # 리스트 l에서 리스트 f의 헤드 노드의 삽입 위치를 찾는다.
        while l[i] < f[0] : i+=1
        l.insert(i, f[0])
        f.popleft()
    
    return l

if __name__ == "__main__" :
    l = deque([2,6,8,9,15,17,34,37,68,86])
    f = deque([1,3,5,6,7,9,11,15,16,17,23,46,52,64])
    r = combine_two_chain(l,f)
    print(r)