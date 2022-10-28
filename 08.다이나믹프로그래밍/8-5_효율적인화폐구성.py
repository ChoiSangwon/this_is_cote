from re import L


N,M = map(int,input().split())
dp=[10001 for _ in range(M+1)]
dp[0]=0
arr=[]
for i in range(N):
    arr.append(int(input()))

for i in range(N):
    for j in range(arr[i],M+1):
        if( dp[j-arr[i]]!=10001):
            dp[j] = min(dp[j],dp[j-arr[i]]+1)

if(dp[M]==10001):
    print(-1)
else:
    print(dp[M])

