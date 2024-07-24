T = [100000]
k = 1
if len(T) <= 10:
    for N in T:
        if N <= 100000 and N >= 1:
            z = "Case "+str(k)+":"
            for y in range(1,N+1):
                if N % y == 0:
                    z = z + " "+ str(y)
            k+=1
            print(z)
        else:
            print("1<=N>=100000")
else:
    print("T<=10")