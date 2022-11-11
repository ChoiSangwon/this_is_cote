N,M = map(int,input().split())
arr = [i for i in range(N+1)]
for i in range(M):
    a,b,c = map(int,input().split())
    if a==0:
        arr[c]=arr[b]