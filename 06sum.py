T = [12345, 56789, 14310, 10062, 96587]
if len(T) <= 10000 and len(T)>= 1:
    for N in T:
        if int(N/10000) <= 9 and int(N/10000) >= 1:
            L = N % 10
            G = N /10000
            M = int(G)
            sum = L + M
            print("Sum = "+str(sum))
        else:
            print("Please enter 5 digit number")    
else:
    print("1<= T <= 10000")