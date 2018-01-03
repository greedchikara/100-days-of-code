def mergesort(input_array, temp, l, r):
    count = 0
    if l < r:
        m = (l + r) / 2
        count = mergesort(input_array, temp, l, m)
        count += mergesort(input_array, temp, m + 1, r)
        count += merge(input_array, temp, l, m, r)
    return count


def merge(input_array, temp, l, m, r):
    count = 0
    leftEnd = m
    rightEnd = r

    left = l
    right = m + 1
    
    index = 0
    
    while left <= leftEnd and right <= rightEnd:
        if input_array[left] <= input_array[right]:
            temp.append(input_array[left])
            left += 1
        else:
            temp.append(input_array[right])
            count = count + ((m+1) - left)
            right += 1
        index += 1

    while left <= leftEnd:
        temp.append(input_array[left])
        index += 1
        left += 1

    while right <= rightEnd:
        temp.append(input_array[right])
        index += 1
        right += 1

    index = 0
    for i in range(l, r + 1):
        input_array[i] = temp[index]
        index += 1
    return count


# input_array = [12, 11, 13, 5, 6, 7]
input_array = [1, 6, 3, 2, 5]
n = len(input_array)
temp = []
print mergesort(input_array, temp, 0, n - 1)
