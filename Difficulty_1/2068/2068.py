t=int(input())
for i in range(t):
    ans=-1
    l=list(map(int,input().split()))
    for j in l:
        if j>ans:
            ans=j


    print("#{} {}".format(i+1,ans))