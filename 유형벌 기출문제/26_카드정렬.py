import sys
from queue import PriorityQueue
input=sys.stdin.readline

q=PriorityQueue(maxsize=100001)
n=int(input())
for i in range(n):
    q.put(int(input()))
res=0
while q.qsize()!=1:
    a=q.get()
    b=q.get()
    res+=a+b
    q.put(a+b)
print(res)