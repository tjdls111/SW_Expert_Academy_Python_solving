n=int(input())
l=list(map(int,input().split()))
l.sort()
print(l[n//2])