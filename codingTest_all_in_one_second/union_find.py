def find(x) :
    if parent[x] != x :
        return find(parent[x])
    return x

def union(x, y) :
    parent[find(y)] = find(x)

parent = [i for i in range(10)]

union(0, 1)
union(1, 2)
union(2, 8)
union(2, 4)
union(3, 6)
union(6, 9)
union(8, 9)
print(parent)
print(find(9))