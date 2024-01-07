def divide_with_logic(x, y) :
    q = 0
    while x >= y :
        shamt = 0
        while (y << shamt) <= x :
            shamt = shamt + 1
        shamt = shamt - 1
        x = x - (y << shamt)
        q = q + (1 << shamt)
    return q

def divide_with_top_down(x, y) :
    sign = 1
    if(x == 0) : 
        return 0
    if (x < 0 and y > 0) or (x > 0 and y < 0) :
        sign = -1
    
    if(x < 0) : x = ~(x) + 1
    if(y < 0) : y = ~(y) + 1
    
    q = 0
    shamt = 31
    while x >= y :
        while (y << shamt > x) :
            shamt = shamt - 1
        x = x - (y << shamt)
        q = q + (1 << shamt)
    if sign < 0 :
        q = ~q + 1
    return q

if __name__ == "__main__" :
    print(divide_with_top_down(-11, 2))