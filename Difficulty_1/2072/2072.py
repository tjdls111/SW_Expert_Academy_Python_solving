t=int(input())
for j in range(t):
    l=list(map(int,input().split()))
    ans=0
    for i in l:
        if i%2!=0:
            ans+=i
    print("#{} {}".format(j+1,ans))