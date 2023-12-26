ls = [i for i in input().split()]
ls1 = []

for i, v in enumerate(ls):
    if v in ls[i+1::]:
        ls1.append(v+"s")
        ls.descard(v)
    else:
        ls1.append(v)
        
print(set(ls1))