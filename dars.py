# def Tub(num: int):
#     s=0
#     if num>0:
#         for i in range(2,num+1):
#             for j in range(2, int(i**0.5)+1):
#                 if i%j==0:
#                     break
#             else:
#                 s+=1
#     print(f"{num} gacha bo'lgan tub sonlar {s} ta!!!")
# n = int(input("n = "))
# Tub(n)

#-------------------------------------------------------------------------------
# a=int(input("a = "))
# n=int(input("n = "))
# sum=0
# for i in range(1, n+1):
#     sum+=int(str(a)*i)
#     print(str(a)*i, sep=' ', end=' ')
#     if i<n:
#         print("+", sep=' ', end=' ')
#     else:
#         print("=",sum)

#-------------------------------------------------------------------------------
def addToArrayForm(num, k: int):
    for i in reversed(range(len(num))):
      k, num[i] = divmod(num[i] + k, 10)

    while k > 0:
      num = [k % 10] + num
      k //= 10

    return num
print(addToArrayForm([1,2,3], 34))
    