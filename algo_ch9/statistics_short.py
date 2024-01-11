import collections as c
n,*l=map(int,open(0))
l.sort()
t=c.Counter(l).most_common(2)
print(round(sum(l)/n),l[n//2],t[-(t[0][1]==t[-1][1])][0],l[-1]-l[0])