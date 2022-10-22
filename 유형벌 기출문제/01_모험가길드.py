N = int(input())
arr = list(map(int,input().split()))
arr.sort()
count=1
res=0
for i in arr:
    if(count>=i):
        res+=1
        count=1
        continue
    count+=1
print(res)
 