from collections import deque
import sys
N,M,K,X = map(int,input().split())
arr = [[] for i in range(N+1)]
check = [0 for i in range(N+1)]
res=[]
for i in range(M):
    a,b= map(int,sys.stdin.readline().split())
    arr[a].append(b)
res=[]
q=deque()
check[X]=-1
for i in arr[X]:
    q.append((i,1))
    check[i]=1
while(len(q)!=0):
    c,count = q.popleft()
    if(check[c]==0):
        check[c]=count
    else:
        check[c]=min(count,check[c])
    for i in arr[c]:
        if(check[i]==0):
            q.append((i,count+1))
aaa=0
for i in range(N+1):
    if check[i]==K:
        aaa+=1
        print(i)
if(aaa==0):
    print(-1)