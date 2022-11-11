def solution(s):
    answer=len(s)
    for i in range(1,len(s)//2+1):
        arr = ''
        count=1
        cur=s[0:i]
        for j in range(i,len(s),i):
            if(cur==s[j:j+i]):
                count+=1
            else:
                if(count==1):
                    arr+=cur
                else:
                    arr+=str(count)+cur
                    count=1
                cur=s[j:j+i]
        if(count==1):
            arr+=cur
        else:
            arr+=str(count)+cur
            
        if(answer>len(arr)):
            answer=len(arr)
    return answer