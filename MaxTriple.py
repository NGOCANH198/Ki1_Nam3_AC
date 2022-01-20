t = int(input())
for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    if (n<3):
        print(sum(a))
    else:
        max1 = max(a)
        a.remove(max1)
        max2 =max(a)
        a.remove(max2)
        max3 = max(a)
        print(max1+max2+max3)