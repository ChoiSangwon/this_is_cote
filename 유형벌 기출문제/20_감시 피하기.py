from itertools import combinations
from copy import deepcopy
N = int(input())
arr = [ list(input().split()) for i in range(N)]
black = []
teacher = []
def solve(arr):
    for i,j in teacher:
        if(i>0)

    return True

for i in range(N):
    for j in range(N):
        if(arr[i][j]=='X'):
            black.append((i,j))
        elif(arr[i][j]=='T'):
            teacher.append((i,j))
wall = list(combinations(black,3))

for i,j,k in wall:
    bbb = deepcopy(arr)
    bbb[i[0]][i[1]]='O'
    bbb[j[0]][j[1]]='O'
    bbb[k[0]][k[1]]='O'
    
# from itertools import combinations
 
# dd = ((-1, 0), (0, 1), (1, 0), (0, -1))
# n = int(input())
# graph = [[' '] for _ in range(n + 1)]
# empty = list()
# teachers = list()
# for i in range(1, n + 1):
#     graph[i] += input().split()
#     for j in range(1, n + 1):
#         if graph[i][j] == 'X':
#             empty.append((i, j))
#         elif graph[i][j] == 'T':
#             teachers.append((i, j))
 
# for obj in combinations(empty, 3):
#     for y, x in obj:
#         graph[y][x] = 'O'
 
#     flag = False
#     for teacher in teachers:
#         for i in range(4):
#             y, x = teacher
#             while 1 <= y <= n and 1 <= x <= n and graph[y][x] != 'O':
#                 if graph[y][x] == 'S':
#                     flag = True
#                     break
#                 y += dd[i][0]
#                 x += dd[i][1]
#             if flag:
#                 break
#         if flag:
#             break
 
#     if not flag:
#         print('YES')
#         exit()
 
#     for y, x in obj:
#         graph[y][x] = 'X'
 
# print('NO')

