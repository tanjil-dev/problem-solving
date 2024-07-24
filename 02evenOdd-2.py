T = ["100", "0", "111"]
if len(T) <= 100 and len(T) >= 1:
    for x in T:
        if int(x) % 2 == 0:
            print("even")
        else:
            print("odd")
else:
    print("Total input range 1 to 100")
