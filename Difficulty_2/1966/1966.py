T=int(input())
for i in range(T):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    print("#{}".format(i+1),end=' ')
    for j in l:
        print(j,end=' ')
    print()
