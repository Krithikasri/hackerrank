n = int(input())
a = list(map(int, input().split()))
x=max(a)
while max(a)==x:
    a.remove(max(a))
print(max(a))
