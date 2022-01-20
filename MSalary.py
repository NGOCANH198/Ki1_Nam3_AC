def BH(LCB):
    BHXH = LCB * 8 / 100
    BHYT = LCB * 1,5 / 100
    BHTN = LCB * 1 / 100
    DP = LCB * 1 / 100
    return round(BHXH + BHYT + BHTN + DP)
def TNCN(TNTT):
    if TNTT <= 5000000:
        res = TNTT * 5 / 100
    elif TNTT <= 10000000:
        res =  (TNTT - 5000000) * 10 / 100 + 250000
    elif TNTT <= 18000000:
        res =  (TNTT - 10000000) * 15 / 100 + 750000
    elif TNTT <= 32000000:
        res =  (TNTT - 18000000) * 20 / 100 + 1950000
    elif TNTT <= 52000000:
        res = (TNTT - 32000000) * 25 / 100 + 4750000
    elif TNTT <= 80000000:
        res =  (TNTT - 52000000) * 30 / 100 + 9750000
    else:
        res =  (TNTT - 52000000) * 35 / 100 + 18150000
        return res
        
t = int(input())
if t < 0  or t > 10:
    print("INVALID INPUT")
else:
    for i in range(t):
        m,n = map(int, input().split())
        if m < 1000 or n < 1000:
            print("INVALID INPUT")
        else:
            print(BH(n), TNCN(m))