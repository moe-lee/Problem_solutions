from LinkedList import Forward_list

def circular_shift_right(l, k) :
    tail = l.head
    n = 0
    while tail.next is not None :
        tail = tail.next
        n += 1
    k = k % n
    tail.next = l.head.next
    #강제적으로 사이클을 형성한다.
    #원형 연결 리스트를 이용해 쉬프트를 구현한다.
    #k번 right-circular-shift 한 결과는 n-k번 left-circular-shift한 결과와 같다.
    for i in range(n - k) :
        tail = tail.next
    l.head.next = tail.next
    tail.next = None
    return l

if __name__ == "__main__" :
    l = Forward_list([2,3,5,3,2])
    l = circular_shift_right(l, 1)
    l.print_all()