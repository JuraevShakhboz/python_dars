st = input(">>> ")
ball = 0
al1 = ['a','e','i','o','u','l','n','s','t','r']
al2 = ['d','g']
al3 = ['b','c','m','p']
al4 = ['f','h','w','v','y']
al5 = ['k']
al6 = ['j','x']
al7 = ['q','z']
for i in st:
    x = i.lower()
    if x in al1:
        ball += 1
    elif x in al2:
        ball += 2
    elif x in al3:
        ball += 3
    elif x in al4:
        ball += 4
    elif x in al5:
        ball += 5
    elif x in al6:
        ball += 8
    elif x in al7:
        ball += 10
print(ball)