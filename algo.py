# Bubble sort
def Bubble(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
a = [0,2,3,4,6,8,9]
print(Bubble(a))

# Selection sort
# def Selection(arr):
#     length = len(arr)
#     for i in range(length-1):
#         minIndex = i
#         for j in range(i+1, length):
#             if arr[j] < arr[minIndex]:
#                 minIndex = j
#         arr[i], arr[minIndex] = arr[minIndex], arr[i]
#     return arr

# a = [1,4,13,15,6,2,9,7,8,5,10,14,11,3,12]
# print(Selection(a))

# Insertion sort
# def Insertion(arr):
#     for step in range(1, len(arr)):
#         key = arr[step]
#         j = step - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j = j - 1
#         arr[j + 1] = key
#     return arr

# a = [1,4,13,15,6,2,9,7,8,5,10,14,11,3,12]
# print(Insertion(a))