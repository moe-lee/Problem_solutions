import copy

def main() :
    m, n, w, h = tuple(map(lambda x : int(x), (input()).split()))
    hr_arr = list(map(lambda x : int(x), (input().split())))
    hr_for_day = list(map(lambda x : int(x), (input().split())))
    ass_plan = [copy.deepcopy([0] * (n)) for i in range(m)]
    
    for i in range(m) :
        
    for i in range(m+1) :
        print(ass_plan[i])
main()