n = int(input())
arr= [0]*n
arr[0]= 1
count=[0,0,0]
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    arr[i] = min(next2, next3, next5)
    if arr[i]==next2:
        count[0]+=1
        next2 = arr[count[0]]*2
    if arr[i]==next3:
        count[1]+=1
        next3 = arr[count[1]]*3
    if arr[i]==next5:
        count[2]+=1
        next5 = arr[count[2]]*5
        
print(arr)     