#선택 정렬
array= [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1,len[array]):
        if array[min_index]>array[j]:
            min_index=j
    array[i], array[min_index] = array[min_index],array[i]
print(array)

#삽입 정렬
array1 = [7,5,9,0,3,1,6,2,4,8]
for i in range(1,len(array1)):
    for j in range(i,0,-1):
        if array1[j] < array1[j-1]:
            array1[j],array1[j-1] = array1[j-1],array1[j]
        else:
            break
print(array1)

#퀵 정렬
array2 = [5,7,9,0,3,1,6,2,4,8]
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side)+[pivot]+ quick_sort(right_side)

print(quick_sort(array2))

#계수 정렬
array3 = [5,7,9,0,3,1,6,2,4,8]
count = [0] * (max(array3)+1)

for i in range(len(array3)):
    count[array[i]]+=1
for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=" ")




