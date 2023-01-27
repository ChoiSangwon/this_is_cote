n = int(input())
data = list(map(int,input().split()))

start = 0
end = len(data) - 1
mid = (start + end) // 2
while start <= end:
    mid = (start + end) // 2

    if data[mid] == mid:
        break  # 함수를 끝내버린다.
    elif data[mid] < mid:
        start = mid + 1
    else:
        end = mid -1
    
if(data[mid]==mid):
    print(mid)
else:
    print(-1)