T=int(input())
for i in range(T):
    l=[0]*1001
    bunho=int(input())
    scores=map(int,input().split())
    for score in scores:
        l[score]+=1
    top=max(l)
    anss=list(filter(lambda x: l[x] == top, range(len(l))))
    print("#{} {}".format(i+1,max(anss)))