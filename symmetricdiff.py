x=int(input())
a=list(map(int,input().split()))
q=set(a)
y=int(input())
b=list(map(int,input().split()))
r=set(b)
s=r.difference(q)
z=q.difference(r)
t=s.union(z)
yy=sorted(t)
for i in range(len(yy)):
    print(yy[i])
