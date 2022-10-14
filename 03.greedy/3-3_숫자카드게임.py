N,M = map(int,input().split())
arr=[]
count=0
for i in range(N):
    tmp = list(map(int,input().split()))
    if(count<min(tmp)):
        count=min(tmp)
    arr.append(tmp)
print(count)