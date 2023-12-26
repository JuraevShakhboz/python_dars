# Rim raqam--------------------------------------------------
# class py_solution:
#     def Rim_raqam(self, num):
#         val = [
#             1000, 900, 500, 400,
#             100, 90, 50, 40,
#             10, 9, 5, 4,
#             1
#             ]
#         syb = [
#             "M", "CM", "D", "CD",
#             "C", "XC", "L", "XL",
#             "X", "IX", "V", "IV",
#             "I"
#             ]
#         roman_num = ''
#         i = 0
#         while  num > 0:
#             for _ in range(num // val[i]):
#                 roman_num += syb[i]
#                 num -= val[i]
#             i += 1
#         return roman_num
# print(py_solution().Rim_raqam(int(input(">>> "))))


# Teskariga o'girish----------------------------------------
# class py_solution:
#     def reverse_words(self, s):
#         return ' '.join(reversed(s.split()))

# print(py_solution().reverse_words(input(">>> ")))

#------------------------------------------------------------
# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if i==j:
#                 continue
#             if nums[i]+nums[j]==target:
#                 return [i, j]

# print(twoSum([15,7,11,2], 9))

#------------------------------------------------------------
def removeElement(nums, val):
        for i in range(len(nums)):
            if nums[i]==val:
                nums.pop(i)
                nums.append("_")
        return nums
print(removeElement([2,3,4,5,2], 2))