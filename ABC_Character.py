import  itertools
n=int(input())
def kt(l,n):
    tong=0
    for i in range(len(l)-1):
        if l[i]>l[i+1]: return 0
        tong+=l[i]
    tong+=l[-1]
    if tong> n :return 1
    return 2
list1=[]
for c in itertools.combinations_with_replacement('123456789', 3):
    l=list(map(int,''.join(c)))
    a=kt(l,n)
    
    if a==2: 
        s=''
        tong=0
        for i in l:tong+=i
        for i in range(len(l)):
            s+=l[i]*chr(ord('A')+i)
        # print(s)
        for p in itertools.permutations(s, tong):
            list12=[]
            list12.append(''.join(p))
            list12.append(tong)
            list1.append(list12)
list1.sort(key = lambda x: x[0])
list1.sort(key = lambda x:int( x[1]),reverse=False)

for i in range (len(list1)):
    if i!= len(list1)-1 and list1[i]!=list1[i-1] :print(list1[i][0])