# 876. Middle of the Linked List
# def middleNode(arr, middle):
#     lst = []
#     for i in range(middle, len(arr)):
#         lst.append(arr[i])
#     return lst
# arr = [1,2,3,4,5,6,7,8]
# print(middleNode(arr, len(arr)//2))

# 206. Reverse Linked List
def ReverseList(arr, high):
    for i in range(len(arr)//2):
        temp = arr[i]
        arr[i] = arr[high-1]
        arr[high-1] = temp
        high-=1
    return arr
lst = [1,2,3,4,5]
print(ReverseList(lst,len(lst)))