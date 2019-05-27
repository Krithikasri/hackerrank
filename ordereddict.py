from collections import OrderedDict

d=OrderedDict()
n=int(input())
for i in range(n):
    item,space,no=input().rpartition(' ')
    d[item]=d.get(item,0)+int(no)
for item,no in d.items():
    print(item,no) 
