arr = input()
res=int(arr[0])
for i in range(1,len(arr)):
    if(arr[i]=='0' or arr[i]=='1' or res==0):
        res+=int(arr[i])
    else:
        res*=int(arr[i])
print(res)