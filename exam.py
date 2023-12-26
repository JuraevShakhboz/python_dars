# 1 - masala
# def naqsh(cols):
#     changes = sum(a != b for a, b in zip(cols, cols[1:]))
#     return changes + len(cols)*2

# lst = ["Blue", "Blue", "Blue", "Red", "Red", "Red"]

# print(naqsh(lst))

# 2 - masala
# def Teskari_Son(txt):
#     d = {'0': '0', '6': '9', '9': '6'}
#     return all(a in d and d[a] == b for a, b in zip(txt, txt[::-1]))

# n = "69069069"
# print(Teskari_Son(n))

# 3 - masala
import re

def phone_number(txt):
    return bool(re.match('^\(\d{3}\) \d{2}-\d{3}-\d{2}-\d{2}$', txt))
    
number = '(998) 93-654-12-78'
print(phone_number(number))

# 4 - masala
# def get_birthday_cake(name, age):
#     char = ['#', '*'][age%2]
#     msg = '{0} {1} Happy Birthday {2}! {1} {0}'.format(char, age, name)
#     wall = char * len(msg)
#     print(f'"{wall}"\n"{msg}"\n"{wall}"')


# get_birthday_cake("Jack", 10)

# 7 - masala
# def can_exit(lst):
#     def step(x, y):
#         if 0<=x<len(lst[0]) and 0<=y<len(lst) and lst[y][x] == 0:
#             lst[y][x] = 2
#             for dx, dy in ((0,-1), (0,1), (-1,0), (1,0)):
#                 step(x+dx, y+dy)
#     step(0, 0)
#     return lst[-1][-1] == 2

# lst = [ [0, 1, 1, 1, 1, 0, 0],
#         [0, 0, 0, 0, 1, 0, 0],
#         [1, 1, 1, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 0],
#         [1, 1, 1, 1, 1, 1, 1] ]

# print(can_exit(lst))