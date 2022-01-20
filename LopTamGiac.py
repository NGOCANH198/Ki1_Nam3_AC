class TamGiac:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def CV(self):
        return self.a + self.b + self.c
    def DT(self):
        if a**2 == b**2+c**2:
            return b*c/2
        if b**2  == a**2 + c**2:
            return a*c/2
        if c**2 == a**2 + b**2:
            return a*b/2
        
a, b, c = map(int, input().split())
if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
    t = TamGiac(a, b, c)
    p = t.CV()
    s = round(t.DT())
    print('{} {}'.format(p,s))
else:
    print("INVALID")