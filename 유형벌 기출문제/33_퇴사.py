N= int(input())
arr=[]
dp=[0]*(N+1)
for i in range(N):
    a,b=map(int,input().split())
    arr.append((a,b))
    dp[i]=b
for i in range(N-1,-1,-1):
    if arr[i][0] + i > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], arr[i][1] + dp[i + arr[i][0]])
print(dp[0])