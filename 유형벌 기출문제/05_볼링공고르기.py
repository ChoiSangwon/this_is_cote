from itertools import combinations
N,M=map(int,input().split())
arr = list(map(int,input().split()))
res = list(combinations(arr,2))
count=0
for i,j in res:
    if(i!=j):
        count+=1
print(count)