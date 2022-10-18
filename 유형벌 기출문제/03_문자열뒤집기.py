arr = input()
count0, count1=0,0
tmp=arr[0]
for i in range(1,len(arr)):
    if(arr[i]!=tmp):
        if(tmp=='1'):
            count1+=1
        else:
            count0+=1
        tmp=arr[i]
if(arr[-1]=='1'):
    count1+=1
else:
    count0+=1
print(min(count1,count0))