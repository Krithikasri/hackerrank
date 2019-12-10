# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
x=list(map(int,input().split()))
m=int(input())
y=list(map(int,input().split()))
s=set(x)
t=set(y)
z=s.intersection(t)
print(len(z))
