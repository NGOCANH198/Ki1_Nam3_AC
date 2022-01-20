import math
class Point:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def Distance(self):
        return math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
class Triangle:
    def __init__(self,c1,c2,c3):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

    def CV(self):
        return self.c1.Distance() + self.c2.Distance() + self.c3.Distance() 

t = int(input())
a=[]
for i in range(t):
    a = list(map(int,input().split()))
    x,y = (a[2] - a[0],a[3] - a[1]),(a[2] - a[4],a[3] - a[5])
    # print(x,y.sep=" ",end=" ")
    if x[0]*y[1] != x[1]*y[0]:
        p1 = Point(a[0], a[1], a[2], a[3])
        p2 = Point(a[0], a[1], a[4], a[5])
        p3 = Point(a[2], a[3], a[4], a[5])

        tri1 = Triangle(p1, p2, p3)
        res = round(tri1.CV(), 3)
        print(res,end ="")
    else:
        print("INVALID")