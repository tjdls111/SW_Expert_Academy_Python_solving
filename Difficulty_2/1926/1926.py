n=int(input())

for i in range(1,n+1):
    if str(i).count('3')+str(i).count('6')+str(i).count('9'):
        cnt='-'*str(i).count('3')+'-'*str(i).count('6')+'-'*str(i).count('9')
        print(cnt,end=' ')
    else:
        print(i,end=' ')
        