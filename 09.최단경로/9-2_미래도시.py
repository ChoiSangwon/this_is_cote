INF = int(1e9)

N, M = map(int, input().split())

arr = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            arr[a][b] = 0

for i in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            arr[a][b] = min(arr[a][b], arr[a][i] + arr[i][b])

X, K = map(int, input().split())

result = arr[1][K] + arr[K][X]

if result < INF:
    print(result)
else:
    print(-1)