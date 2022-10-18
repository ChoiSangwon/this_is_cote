n = int(input())
arr = list(map(int,input().split()))
arr.sort()
res=1
for i in arr:
    print(res)
    if(res < i):
        break
    res+=i
print(res)