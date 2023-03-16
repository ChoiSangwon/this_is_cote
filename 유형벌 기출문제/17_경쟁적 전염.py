from collections import deque
import sys
from functools import cmp_to_key
input = sys.stdin.readline

def cmp(a,b):
    if a[2]>b[2]:
        return -1
    else:
        return 1

N,K =map(int,input().split())
arr=[]
d=[(0,1),(0,-1),(1,0),(-1,0)]

for i in range(N):
    arr.append(list(map(int,input().split())))
S,X,Y = map(int,input().split())

tmp=[]
for j in range(N):
    for k in range(N):
        if arr[j][k]!=0:
            tmp.append((j,k,arr[j][k],1))
q=deque()
tmp.sort(key=cmp_to_key(cmp))
for i in tmp:
    q.append(i)
while q:
    pa,pb,value,count=q.pop()
    if(count>S):
        break
    for i,j in d:
        ca=pa+i
        cb=pb+j
        if(0<=ca<N and 0<=cb<N and arr[ca][cb]==0):
            arr[ca][cb]=value
            q.appendleft((ca,cb,value,count+1))
print(arr[X-1][Y-1])