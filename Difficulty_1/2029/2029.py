T=int(input())

for i in range(T):
    a,b=map(int,input().split())
    mok=a//b
    nameji=a%b
    print(f"#{i+1} {mok} {nameji}")