N,M = map(int,input().split())
X,Y,Z = map(int,input().split())
check=[[0 for i in range(M)] for j in range(N)]
res=[0]
arr=[]
for i in range(N):
    tmp = list(map(int,input().split()))
    arr.append(tmp)

def solve(i,j):
    res[0]+=1
    check[i][j]=1
    if(i>0 and arr[i-1][j]==0 and check[i-1][j]==0):
        solve(i-1,j)
    if(j>0 and arr[i][j-1]==0 and check[i][j-1]==0):
        solve(i,j-1)
    if(i<N-1 and arr[i+1][j]==0 and check[i+1][j]==0):
        solve(i+1,j)
    if(j<M-1 and arr[i][j+1]==0 and check[i][j+1]==0):
        solve(i,j+1)

solve(X,Y)
print(res[0])