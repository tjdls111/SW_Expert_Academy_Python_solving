T=int(input())
for i in range(T):
    P,Q,R,S,W=map(int,input().split())

    A=P*W
    if R>=W:
        B=Q
    else:
        B=Q+(W-R)*S
    
    if A>B:
        ans=B
    else:
        ans=A
    
    print("#{} {}".format(i+1, ans))
