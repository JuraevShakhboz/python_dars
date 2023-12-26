def Sezar(st, num):
    t = ""
    for i in st:
        t += str(i)+num
    return t



txt = "hello"
n = 5
print(Sezar(txt, n))