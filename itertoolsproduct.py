from itertools import product
A=list(map(int,input().split()))
B=list(map(int,input().split()))
y=list(product(*[A,B]))
for i in y:
    print(i,end=" ")
