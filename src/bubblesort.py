def bubblesort(input_array):
    for j in range(len(input_array)):
        for i in range(len(input_array)):
            if(i < (len(input_array) - 1) and input_array[i] > input_array[i + 1]):
                temp = input_array[i+1]
                input_array[i + 1] = input_array[i]
                input_array[i] = temp
    return input_array

input_array = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print bubblesort(input_array)


# for j in range(len(input_array)):
#         if(j <= 2):
#             for i in range(1, len(input_array)):
#                 if(input_array[i - 1] > input_array[i]):
#                     temp = input_array[i - 1]
#                     input_array[i - 1] = input_array[i]
#                     input_array[i] = temp
#     return input_array
