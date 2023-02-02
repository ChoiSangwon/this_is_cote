import sys
n,c= map(int,input().split())
arr= [0]*n
for i in range(n):
    arr[i]=int(sys.stdin.readline())
arr.sort()
start = 0
end = arr[-1]-arr[0]
mid=(start+end)//2
res=0
while (start<=end):
    mid=(start+end)//2
    count=1
    a=arr[0]
    for i in range(1, n):
    	if arr[i]-a >= mid:
            count += 1
            a=arr[i]
    if count >= c: 
        start = mid + 1
        res = mid
    else: 
    	end = mid - 1
print(res)