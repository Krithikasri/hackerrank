n=int(input())
x=set(list(map(int,input().split())))

y=int(input())
m=set(list(map(int,input().split())))
c=x-m
z=x.symmetric_difference(m)
print(len(z))
