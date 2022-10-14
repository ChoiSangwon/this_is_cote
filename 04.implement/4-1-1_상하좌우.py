N = int(input())
arr = list(map(str,input().split()))
X,Y=1,1
for i in arr:
    if(i=='R' and X<N):
        X+=1
    elif(i=='L' and X>1):
        X-=1
    elif(i=='U'and Y>1):
        Y-=1
    elif(i=='D' and Y<N):
        Y+=1
print(Y,X)