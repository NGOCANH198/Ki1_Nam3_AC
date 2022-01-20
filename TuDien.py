
l = list()
n=int(input())
tich,tong = 1,0
for _ in range(n):
    list1=list(map(str,input().split()))
    l.append(list1)

for i in l:
    if(i[1].isnumeric()):
        tong+= int(i[1])
        tich*= int(i[1])
        
if(n<=10):
    print(tong,tich,sep=" ",end=" ")
    print()
else:
    print("INVALID INPUT")