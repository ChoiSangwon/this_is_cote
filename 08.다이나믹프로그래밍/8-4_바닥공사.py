N =int(input())
dp =[0 for i in range(N)]
dp[0],dp[1] = 1,3
for i in range(2,N):
    dp[i] = (dp[i-1]+2*dp[i-2])%796796
print(dp[N-1])