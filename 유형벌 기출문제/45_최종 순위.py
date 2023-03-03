import sys
from collections import deque
 
T=int(input())
for _ in range(T):
    n=int(sys.stdin.readline())
    ranking=list(map(int,sys.stdin.readline().split()))
    lanking=[[] for _ in range(n+1)]
    indegree=[0 for _ in range(n+1)]
    q=deque()
    for i in range(0,n-1):
        for j in range(i+1,n):
            lanking[ranking[i]].append(ranking[j])
            indegree[ranking[j]]+=1
 
    m=int(input())
    for _ in range(m):
        a,b=map(int,sys.stdin.readline().split())
        check=True
        for i in lanking[a]:
            if i==b:
                lanking[a].remove(b)
                lanking[b].append(a)
                indegree[b]-=1
                indegree[a]+=1
                check=False
        if check:
            lanking[b].remove(a)
            lanking[a].append(b)
            indegree[a] -= 1
            indegree[b] += 1
 
 
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)
 
    res=True  
    resList=[]
    if not q:
        res=False
    while q:
        if len(q)>1:
            res=1
            break
        a=q.popleft()
        resList.append(a)
        for i in lanking[a]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
            elif indegree[i]<0:
                res=False
                break
 
    if res==False or len(resList)<n:
        print('IMPOSSIBLE')
    else:
        print(*resList)
 
