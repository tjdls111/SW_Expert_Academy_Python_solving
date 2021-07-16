t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    l.sort()
    print(l)
    del l[-1]
    del l[0]
    print(l)
    ans=round(sum(l)/8)
    print(ans)

    print(f"#{i+1} {int(ans)}")