t = int(input())
if t < 0 or t > 10:
    print("INVALID INPUT")
else:
    while t > 0:
        t -= 1
        n = int(input())
        if  n > 365:
            print("INVALID INPUT")
        else:
            a = 0
            while n >= 11:
                a += (a + 1)
                n -= 11
            print(a)