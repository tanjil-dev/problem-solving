T = [100, 0, 111]
if len(T) <= 100 and len(T) >= 1:
    for x in T:
        if x % 2 == 0 and x >=0 and x<=2147483647:
            print("even")
        elif x >=0 and x<=2147483647:
            print("odd")
        else:
            print("Input range 0 to 2147483647")
else:
    print("Total input range 1 to 100")
