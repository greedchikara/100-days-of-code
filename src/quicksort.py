def quicksort(input_array, l, h):
    if l < h:

        pivot = partition(input_array, l, h)
        quicksort(input_array, l, pivot - 1)
        quicksort(input_array, pivot + 1, h)

def partition(input_array, l, h):

    pivot = input_array[h]
    i = l - 1

    for j in range(l, h):
        if input_array[j] <= pivot:
            i += 1
            temp = input_array[i]
            input_array[i] = input_array[j] 
            input_array[j] = temp
        
    input_array[h] = input_array[i + 1]
    input_array[i + 1] = pivot
    return (i + 1)

input_array = [1, 3, 4, 2, 5]
n = len(input_array) - 1
quicksort(input_array, 0, n)

print input_array