t=int(input())

for i in range(t):
    a,b=map(int,input().split())

    if a==b:
        ans='='
    elif a>b:
        ans='>'
    else:
        ans='<'
    
    print("#{} {}".format(i+1,ans))