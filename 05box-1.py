T = [1,3,5]
if len(T)<=25 and len(T)>=1:
    u = len(T)
    for x in T:
        if x <= 80 and x >=1:
            k = x
            y = x
            while x > 0:
                z = ""  
                if x < y:
                    k = y  
                while k > 0:
                    z = z + "*"
                    k-=1
                print(z)
                x-=1
            u -=1
            if u > 0:
                print("\n")
        else:
            print("number between 1-80")
else:
    print("1<=T<=25")