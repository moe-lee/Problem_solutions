T = int(input())
tbl = {
    'ZRO' : 0,'ONE' : 1, 'TWO' : 2, 'THR' : 3, 'FOR' : 4,'FIV' : 5,'SIX' : 6,'SVN' : 7,'EGT' : 8,'NIN' : 9
}

for test_case in range(T):
    prefix, N = input().split()
    N = int(N)
    words = input().split()
    words.sort(key = lambda x : tbl[x])
    print(prefix)
    print(*words)