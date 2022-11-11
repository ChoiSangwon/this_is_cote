from itertools import permutations
N = int(input())
arr = list(map(int,input().split()))
a,b,c,d = map(int,input().split())
maxRes=-100000000
minRes=100000000
def DFS(count,res):
    global a,b,c,d,maxRes,minRes
    if(count==N-1):
        maxRes=max(maxRes,res)
        minRes=min(minRes,res)
    if(a>0):
        a-=1
        DFS(count+1,res+arr[count+1])
        a+=1
    if(b>0):
        b-=1
        DFS(count+1,res-arr[count+1])
        b+=1
    if(c>0):
        c-=1
        DFS(count+1,res*arr[count+1])
        c+=1
    if(d>0):
        d-=1
        DFS(count+1,int(res/arr[count+1]))
        d+=1
DFS(0,arr[0])
print(maxRes)
print(minRes)