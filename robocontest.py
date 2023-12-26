import math
a,b,c,d,e = map(int, input().split())
s = a+b+c+d+e
mn = min(a,b,c,d,e)
mx = max(a,b,c,d,e)
mn_res = s - mx
mx_res = s - mn
print(mn_res, mx_res)