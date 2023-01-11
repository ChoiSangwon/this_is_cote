from functools import cmp_to_key


def solve(arr1,arr2):
    if(arr1[1]<arr2[1]):
        return 1
    elif(arr1[1]>arr2[1]):
        return -1
    else:
        if arr1[2]>arr2[2]:
            return 1
        elif arr1[2]<arr2[2]:
            return -1
        else:
            if arr1[3]<arr2[3]:
                return 1
            elif arr1[3]>arr2[3]:
                return -1
            else:
                if arr1[0]>arr2[0]:
                    return 1
                else:
                    return -1

N = int(input())
arr=[]
for i in range(N):
    name,K,E,M = input().split()
    arr.append((name,int(K),int(E),int(M)))
arr = sorted(arr,key=cmp_to_key(solve))
for i in arr:
    print(i[0])