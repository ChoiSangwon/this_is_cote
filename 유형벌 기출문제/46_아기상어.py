from collections import deque
from functools import cmp_to_key
n = int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
ci,cj=0,0
d = [(-1,0),(0,-1),(1,0),(0,1)]
sharkWidth=2

def aaa(a,b):
    if a[0]>b[0]:
        return 1
    elif a[0]<b[0]:
        return -1
    else:
        if a[1]>b[1]:
            return 1
        else:
            return -1

def PossibleLocation(i,j):
    global n,sharkWidth
    q= deque()
    q.append((i,j,0))
    check=[[0 for _ in range(n)]for _ in range(n)]
    check[i][j]=1
    res=[]
    while q:
        pi,pj,count=q.popleft()
        if(arr[pi][pj]!=0 and arr[pi][pj]!=9 and arr[pi][pj]>0 and sharkWidth>arr[pi][pj] ):
            res.append((pi,pj,count))
        else:
            for k in range(4):
                ti = pi+d[k][0]
                tj = pj+d[k][1]
                if(0<=ti<n and 0<=tj<n and check[ti][tj]==0 and arr[ti][tj]<=sharkWidth):
                    check[ti][tj]=1
                    q.append((ti,tj,count+1))
    return res


for i in range(n):
    for j in range(n):
        if(arr[i][j]==9):
            ci=i
            cj=j
eatfish=0
totalCount=0
while True:
    curLocate=PossibleLocation(ci,cj)
    if(len(curLocate)==0):
        print(totalCount)
        exit()
    elif(len(curLocate)==1):
        totalCount+=curLocate[0][2]
        arr[ci][cj]=0
        ci=curLocate[0][0]
        cj=curLocate[0][1]
        arr[ci][cj]=9
        eatfish+=1
    else:
        lowerCount=100000000
        for li,lj,count in curLocate:
            if(lowerCount>count):
                lowerCount=count
        tmpArr=[]
        for li,lj,count in curLocate:
            if(count==lowerCount):
                tmpArr.append((li,lj))
        tmpArr.sort(key=cmp_to_key(aaa))
        totalCount+=lowerCount
        arr[ci][cj]=0
        ci=tmpArr[0][0]
        cj=tmpArr[0][1]
        arr[ci][cj]=9
        eatfish+=1
    if(eatfish==sharkWidth):
        sharkWidth+=1
        eatfish=0
