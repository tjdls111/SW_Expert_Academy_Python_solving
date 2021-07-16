headline=input()
for i in headline:
    if 97<=ord(i)<=122:
        print(chr(ord(i)-32),end='')
    else:
        print(i,end='')