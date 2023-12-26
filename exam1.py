# 2 - masala | DONUTS
# def duplicateZeros(arr):
#     zeros = []

#     for i in arr:
#         if i == 0:
#             zeros.append(i)
#             zeros.append(i)
#         else:
#             zeros.append(i)
#     return zeros

# arr = [100, 10, 0, 101, 1000]
# print(duplicateZeros(arr))


# 4 - masala | C/C++ COMPILER

f = open("C_code.txt", "a+")

for i in f.read().split("\n"):
    x = i.strip()
    y = x[0]+"="+x[0]+"+"+"1"+";"
    if y==i.strip():
        f.write(x[0]+"++;")

f.close()