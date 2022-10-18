#1. 스택
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])

#2. 큐
from collections import deque
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

#3. 재귀 함수
def recursive_function():
    print("재귀함수 호출")
    recursive_function()
recursive_function()
# > 종료조건이 없이 무한히 돌다가 오류 난다

#4. 재귀 함수의 종료 조건
def recursive_function1(i):
    if i== 100:
        return
    print(i, "번째 재귀 함수에서", i+1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i,'번째 재귀 함수를 종료합니다.')
recursive_function1(1)

#5. 팩토리얼 예제
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result =1
    for i in range(1,n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_iterative1(n):
    if(n<=1):
        return 1
    return n*factorial_iterative1(n-1)

print("반복적으로 구현:",factorial_iterative(5))
print("재귀적으로 구현:",factorial_iterative1(5))