def mergesort(input_array, l, r):
    if l < r:
        m = (l + r) / 2
        mergesort(input_array, l, m)
        mergesort(input_array, m+1, r)
        merge(input_array, l, m, r)

def merge(input_array, l, m, r):
    leftEnd = m
    rightEnd = r

    left = l
    right = m + 1

    temp = []
    index = 0

    while left <= leftEnd and right <= rightEnd:
        if input_array[left] <= input_array[right]:
            temp.append(input_array[left])
            left += 1
        else:
            temp.append(input_array[right])
            right += 1
        index += 1
    
    while left <= leftEnd:
        temp.append(input_array[left])
        index += 1
        left +=1
    
    while right <= rightEnd:
        temp.append(input_array[right])
        index += 1
        right += 1
    print input_array
    print temp
    index = 0
    for i in range(l, r + 1):
        input_array[i] = temp[index]
        index += 1


input_array = [12, 11, 13, 5, 6, 7]
n = len(input_array)

mergesort(input_array, 0, n - 1)

for i in range(n):
    print ("%d" % input_array[i]),
