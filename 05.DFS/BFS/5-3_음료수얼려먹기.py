N,M = map(int,input().split())
visit = [[0 for _ in range(M)] for _ in range(N)]
res = []
for i in range(N):
    tmp = input()
    res.append(tmp)

def dfs(i,j):
    visit[i][j]=1
    if(i>0 and visit[i-1][j]==0 and res[i-1][j]=="0"):
        dfs(i-1,j)
    if(j>0 and visit[i][j-1]==0 and res[i][j-1]=="0"):
        dfs(i,j-1)
    if(i<N-1 and visit[i+1][j]==0 and res[i+1][j]=="0"):
        dfs(i+1,j)
    if(j<M-1 and visit[i][j+1]==0 and res[i][j+1]=="0"):
        dfs(i,j+1)

count=0
for i in range(N):
    for j in range(M):
        if(visit[i][j]==0 and res[i][j]=='0'):
            dfs(i,j)
            count+=1
print(count)