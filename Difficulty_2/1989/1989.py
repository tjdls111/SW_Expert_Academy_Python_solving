T=int(input())

for i in range(T):
    n=input()
    if n==n[::-1]:
        ans=1
    else:
        ans=0
    print(f"#{i+1} {ans}")