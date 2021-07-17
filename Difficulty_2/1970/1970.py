T=int(input())
moneys=[50000,10000,5000,1000,500,100,50,10]
for i in range(T):
    n=int(input())
    now=n
    l=[0]*8
    for j in range(len(moneys)):
        if now//moneys[j]>0:
            m=now//moneys[j]
            now=now-moneys[j]*m
            l[j]=m
    print(f"#{i+1}")
    for x in l:
        print(x,end=' ')
    print()


    