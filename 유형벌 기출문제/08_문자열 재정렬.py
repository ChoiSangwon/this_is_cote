arr = input()
alpha =[]
res=0
for i in arr:
    if(i<='9' and i>='0'):
        res+=int(i)
    else:
        alpha.append(i)
alpha.sort()
print(''.join(alpha),end="")
print(res)