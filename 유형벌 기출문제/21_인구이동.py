from collections import deque
N,L,R=map(int,input().split())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))

def solve(arr,arr2,i,j,count,res):
    res=arr[i][j]
    

q=deque()
q.appendleft((0,0,0))
while True:
    

