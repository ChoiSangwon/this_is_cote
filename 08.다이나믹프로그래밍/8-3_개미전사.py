N = int(input())
arr = list(map(int,input().split()))
dp = [0 for i in range(N+2)]
for i in range(N):
    dp[i+2]=max(dp[i+1],dp[i]+arr[i])
print(dp[N+1]) 