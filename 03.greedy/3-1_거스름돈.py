N = int(input())
res=0
res+=N//500
N-=500*(N//500)
res+=N//100
N-=100*(N//100)
res+=N//50
N-=50*(N//50)
res+=N//10
print(res)