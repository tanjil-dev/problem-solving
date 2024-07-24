x = 1000
p = []
while x > 0:
    p.append(x)
    if len(p) == 5:
        s = ""
        for y in p:
            s = s + str(y) + "\t"
        p = []    
        print(s)    
    x-=1