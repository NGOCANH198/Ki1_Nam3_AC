def cs(s):
    so = 0
    for i in range(0, len(s),1):
        if s[i] == "0":
            so+= 2**(len(s) - i - 1)
    return so    

def solve(n, b):
    res = ""
    while (n > 0):
        m = n % b
        if m >= 10: res += str(chr(55 + m))
        else: res += str(m)
        n=n//b
    print(res[::-1])

a = []
for i in lines:
  a.append(i.strip())
t = int(a[0])
x,y = 1,2
for i in range(t):
    x+=2
    y+=2
    n = int(a[x])
    s = a[y]
    solve(cs(s), n)
