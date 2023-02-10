#회전시키는 함수
def rotate(arr):
    n = len(arr)
    tmp = [[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[j][n-i-1]=arr[i][j]
    return tmp

#현재 열쇠가 lock에 맞는지를 확인하는 함수
def check(res,locklen):
    for i in range(locklen,locklen*2):
        for j in range(locklen,locklen*2):
            if(res[i][j]!=1):
                return False
    return True

def pANDm(key,res,keylen,plus,ci,cj):
    if(plus):
        for i in range(keylen):
            for j in range(keylen):
                res[ci+i][cj+j]+=key[i][j]
    else:
        for i in range(keylen):
            for j in range(keylen):
                res[ci+i][cj+j]-=key[i][j]


def solution(key, lock):
    answer = True
    locklen = len(lock)
    keylen=len(key)
    res=[[0 for i in range(locklen*3)] for j in range(locklen*3)]
    for i in range(locklen):
        for j in range(locklen):
            res[i+locklen][j+locklen]=lock[i][j]
    for k in range(4):
        key=rotate(key)
        for i in range(1,locklen*2):
            for j in range(1,locklen*2):
                pANDm(key,res,keylen,True,i,j)
                if(check(res,locklen)):
                    return True
                pANDm(key,res,keylen,False,i,j)
    return False