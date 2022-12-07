from itertools import combinations
from copy import deepcopy
import sys
sys.setrecursionlimit(10000000)

N,M=map(int,input().split())
ax=[0,0,1,-1]
ay=[1,-1,0,0]
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

def solve(a,b,arr):
    arr[a][b]=2
    if(a>0 and arr[a-1][b]==0):
        solve(a-1,b,arr)
    if(b>0 and arr[a][b-1]==0):
        solve(a,b-1,arr)
    if(a<N-1 and arr[a+1][b]==0):
        solve(a+1,b,arr)
    if(b<M-1 and arr[a][b+1]==0):
        solve(a,b+1,arr)

V =[]
two = []
for i in range(N):
    for j in range(M):
        if(arr[i][j]==0):
            V.append((i,j))
        if(arr[i][j]==2):
            two.append((i,j))

b= list(combinations(V,3))
maxRes = 0
for i in b:
    res = deepcopy(arr)
    for q,w in i:
        res[q][w]=1
    for q,w in two:
        solve(q,w,res)
    tmp=0
    for j in range(N):
        tmp+=res[j].count(0)
    maxRes=max(tmp,maxRes)
    # print(res)
print(maxRes)
