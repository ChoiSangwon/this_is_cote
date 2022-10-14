N,K = map(int,input().split())

def solve(a,count):
    if(a==1):
        print(count)
        exit()
    if(a%K==0):
        solve(a//K,count+1)
    else:
        solve(a-1,count+1)

solve(N,0)