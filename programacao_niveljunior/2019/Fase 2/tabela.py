j,p,v,e,d = map(int, input().split())

if j == -1:
    if v != -1 and e != -1 and d != -1:
        j = v+e+d
    else:
        if v == -1 and e != -1 and p != -1:
            v = (p-e)/3
        if e == -1 and p != -1 and v != -1:
            e=p-3*v
            if e < -1:
                e=e*(-1)
        if d != -1:
            j=v+e+d
if v == -1:
    if j != -1 and e != -1 and d != -1:
        v=j-e-d
if e == -1:
    if j != -1 and v != -1 and d != -1:
        e=j-v-d
if d == -1:
    if j != -1 and v != -1 and e != -1:
        d=j-v-e
if p == -1:
    if v != -1 and e != -1:
        p = 3*v+e

print(int(j),int(p),int(v),int(e),int(d))
