import sys
from collections import deque
input = sys.stdin.readline

N,M=map(int,input().split())
arr={}
check = [0]*(N+1)
for i in range(1,N+1):
    arr[i]=[]
for i in range(M):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

q=deque()

q.append((1,1))
check[1]=1
while q:
    a,count = q.popleft()
    for i in arr[a]:
        if(check[i]==0):
            check[i]=count+1
            q.append((i,count+1))
print(check.index(max(check)),max(check)-1,check.count(max(check)))