T = int(input())
for i in range(T):
    n,m = map(int,input().split())
    tmp=list(map(int,input().split()))
    arr=[[0 for _ in range(m+1)] for _ in range(n+2)]
    dp=[[0 for _ in range(m+1)] for _ in range(n+2)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            arr[i][j]=tmp[(i-1)*m+j-1]
    for i in range(1,n+1):
        dp[i][1]=arr[i][1]
    for j in range(2,m+1):
        for i in range(1,n+1):
            dp[i][j]=max(dp[i][j-1],dp[i-1][j-1],dp[i+1][j-1])+arr[i][j]
    res=dp[1][m]
    for i in range(2,n+1):
        if(dp[i][m]>res):
            res=dp[i][m]
    print(res)
    
