t=int(input())
for cnt in range(t):
    n=int(input())
    ans=0
    for i in range(1,n+1):
        if i%2==0:
            ans-=i
        else:
            ans+=i
    print(f"#{cnt+1} {ans}")
