N = int(input())
res=[]
for i in range(N):
    tmp = input().split()
    res.append((tmp[0],int(tmp[1])))
res = sorted(res, key=lambda student: student[1])

for student in res:
    print(student[0],end=" ")