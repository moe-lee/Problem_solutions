hours, minutes = map(int, input().split())
offset = int(input())
minutes += offset
hours += minutes // 60
minutes %= 60
hours %= 24
print(hours, minutes)