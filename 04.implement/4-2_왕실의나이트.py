N = input()
X=int(ord(N[0]))-int(ord('a'))+1
Y=int(N[1])
arr = [(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(-1,-2),(-1,2),(1,-2)]
count=0
for i,j in arr:
    if(X+i>0 and Y+j>0 and X+i<=8 and Y+j<=8):
        count+=1
print(count)