t = int(input())

for i in range(0,t):
    n = int(input())
    a = [int(i) for i in input().split()]
    if (n<3):
        print(sum(a))
    else:
        min1 = min(a)
        a.remove(min1)
        min2 =min(a)
        a.remove(min2)
        min3 = min(a)
        print(min1+min2+min3)