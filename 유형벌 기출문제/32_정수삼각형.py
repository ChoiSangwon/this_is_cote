n= int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
dp=[[0]*(i+1) for i in range(n)]
if(n==1):
    print(arr[0][0])
else:
    dp[0][0]=arr[0][0]
    dp[1][0]=dp[0][0]+arr[1][0]
    dp[1][1]=dp[0][0]+arr[1][1]
    for i in range(2,n):
        for j in range(i+1):
            if(j==0):
                dp[i][j]=dp[i-1][j]+arr[i][j]
            elif j==i:
                dp[i][j]=dp[i-1][j-1]+arr[i][j]
            else:
                dp[i][j]=max(dp[i-1][j]+arr[i][j],dp[i-1][j-1]+arr[i][j])
    print(max(dp[n-1]))

