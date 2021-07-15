t=int(input())
for i in range(t):
    addAll=0
    l=list(map(int,input().split()))
    for j in l:
        addAll+=j
    #print(addAll/10)
    if int(str(addAll/10)[-1])>=5:
        ans=int(str(addAll/10)[:-2])+1
    else:
        ans=int(str(addAll/10)[:-2])
    print("#%d %d" %(i+1,ans))
    #print("#%d %d" %(i+1,ans))