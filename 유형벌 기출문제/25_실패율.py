def solution(N, stages):
    answer=[]
    res={}
    count=len(stages)
    for i in range(1,N+1):
        if(count>0):
            tmp=stages.count(i)
            res[i]=tmp/count
            count-=tmp
        else:
            res[i]=0
    print(res)
    a = sorted(res.items(),reverse=True,key=lambda x: x[1])
    for i in a:
        answer.append(i[0])
    
    return answer