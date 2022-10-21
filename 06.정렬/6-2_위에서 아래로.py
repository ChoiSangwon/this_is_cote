n =  int(input())
res=[]
for i in range(n):
    res.append(int(input()))
res.sort(reverse=True)

for i in res:
    print(i,end=" ")