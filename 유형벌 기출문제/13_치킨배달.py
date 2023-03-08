from itertools import combinations

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
chicken=[]
house=[]
res=10000000

for i in range(N):
    for j in range(N):
        if(arr[i][j]==2):
            chicken.append((i,j))
        elif(arr[i][j]==1):
            house.append((i,j))

aaa= list(combinations(chicken,M))
for i in aaa:
    tmp=0
    for j in house:
        cur=1000000
        for k,l in i:
            cur=abs(j[0]-k)+abs(j[1]-l)
        tmp+=cur
    res=min(res,tmp)
print(res)