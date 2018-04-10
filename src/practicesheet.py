# class Element(object):
    
#     def __init__(self, value):
#         self.value = value
#         self.next = None
        
# class LinkedList(object):
    
#     def __init__(self, head=None):
#         self.head = head
        
#     def append(self, new_element):
        
#         current = self.head
#         if current:
#             while current.next:
#                 current = current.next
#             current.next = new_element
#         else:
#             self.head = new_element

#     def getPosition(self, position):

#         counter = 1
#         current = self.head
#         if position < 1:
#             return None
#         else:
#             while current and position <= counter:
#                 if position == counter:
#                     return current
#                 current = current.next
#                 counter += 1
#         return None
    
#     def printLinkedList(self):
        
#         current = self.head
#         strList = ""
#         while current:
#             strList += str(current.value) + "->"
#             current = current.next
#         print strList

# # Test cases
# # Set up some Elements
# e1 = Element(1)
# e2 = Element(2)
# e3 = Element(3)
# e4 = Element(4)

# # Start setting up a LinkedList
# ll = LinkedList(e1)
# ll.append(e2)
# ll.append(e3)
# ll.append(e4)

# ll.printLinkedList()

# print ll.getPosition(5).value

# Find Largest Continuous sum in an array

# def findLargestContinuousSubArray(array):
#     actualMax = 0
#     maxTillPoint = 0
#     start = 0
#     s = 0
#     end = 0
#     for i in range(len(array)):
#         maxTillPoint += array[i]

#         if actualMax < maxTillPoint:
#             actualMax = maxTillPoint
#             start = s
#             end = i
        
#         if maxTillPoint < 0:
#             maxTillPoint = 0
#             s = i+1
    
#     print "max => " + str(actualMax)
#     print "start index => " + str(start)
#     print "end index => " + str(end)

# findLargestContinuousSubArray([-2, -3, 4, -1, -2, 1, 5, -3])


# merge sort

def mergeSort(array, l, r):
    
    if l < r:
        m = (l + r) / 2
        mergeSort(array, l, m)
        mergeSort(array, m + 1, r)
        merge(array, l, m, r)

def merge(array, l, m, r):
    leftEnd = m
    rightEnd = r

    left = l
    right = m+1

    temp = []

    while left <= leftEnd and right <= rightEnd:
        if array[left] <= array[right]:
            temp.append(array[left])
            left += 1
        else:
            temp.append(array[right])
            right += 1
    
    while left <= leftEnd:
        temp.append(array[left])
        left += 1
    
    while right <= rightEnd:
        temp.append(array[right])
        right += 1
    
    index = 0

    for i in range(l, r+1):
        array[i] = temp[index]
        index += 1


input_array = [12, 11, 13, 5, 6, 7]
n = len(input_array)

mergeSort(input_array, 0, n - 1)

for i in range(n):
    print ("%d" % input_array[i]),

