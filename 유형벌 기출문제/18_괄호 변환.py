from collections import deque

def checkCorret(p):
    check = True
    count=0
    arr = deque()
    for i in range(len(p)):
        if(p[i]=='('):
            arr.append(p[i])
            count+=1
        else:
            if(len(arr)==0):
                check = False
            else:
                arr.pop()
            count-=1
    if(check):
        return 1
    elif(count==0):
        return 2
    else:
        return 3

def check11(p):
    u=""
    v=""
    count1=0
    for j in range(len(p)):
        if(j != 0 and count1==0):
            v=p[j:]
            break
        if(p[j]=='('):
            count1+=1
            u+="("
        else:
            count1-=1
            u+=')'
    return u,v

def solution(p):
    if p=='':
        return p
    answer = ''
    u,v = check11(p)
    check = checkCorret(u)
    if(check==1):
        answer+=u+(solution(v))
    else:
        answer+="("
        answer+=solution(v)
        answer+=")"
        u=u[1:]
        u=u[:-1]
        for i in range(len(u)):
            if(u[i]==")"):
                answer+='('
            else:
                answer+=')'
            
    return answer

