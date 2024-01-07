from copy import deepcopy

steps = { 'R' : (0, 1), 'L' : (0,-1), 'B' : (1, 0), 'T' : (-1, 0), 'RT' : (-1, 1), 'RB' : (1, 1), 'LB':(1, -1), 'LT' : (-1, -1)}

def step_forward(king, stone) :
    drc = steps[input()]
    king_after_step = [king[0] + drc[0], king[1] + drc[1]]
    if king_after_step[0] < 0 or king_after_step[0] >= 8 or king_after_step[1] < 0 or king_after_step[1] >= 8 : return
    
    if king_after_step[0] == stone[0] and king_after_step[1] == stone[1] :
        stone_after_step = [stone[0] + drc[0], stone[1] + drc[1]]
        if stone_after_step[0] < 0 or stone_after_step[0] >= 8 or stone_after_step[1] < 0 or stone_after_step[1] >= 8 :
            return;
        stone[0], stone[1] = stone_after_step[0], stone_after_step[1]
    king[0], king[1] = king_after_step[0], king_after_step[1]

def solve() :
    board = [deepcopy([0] * 8) for i in range(8)]
    row = lambda x : ord('8') - ord(x)
    col = lambda x : ord(x) - ord('A')
    
    k_p, s_p, n = input().split()
    n = int(n)
    king = [row(k_p[1]), col(k_p[0])]
    stone = [row(s_p[1]), col(s_p[0])]
    
    for t_count in range(n) :
        step_forward(king, stone)
        
    print(chr(king[1] + ord('A'))+chr(ord('8') - king[0]))
    print(chr(stone[1] + ord('A'))+chr(ord('8') - stone[0]))
solve()