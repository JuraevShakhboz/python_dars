st = input()
alfabit = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in alfabit:
    if i in st:
        continue
    if i.isdigit() or i.isspace():
        print("ERROR")
    if i not in st:
        print(i)