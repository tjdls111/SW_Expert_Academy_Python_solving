T=int(input())

for i in range(T):
    n=input()
    year=int(n[:4])
    month=int(n[4:6])
    day=int(n[6:])
    #print(year,month,day)
    ans=1
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or  month==12:
        if 1<=day<=31:
            pass
        else:
            ans=-1
    elif month==4 or month==6 or month==9 or month==11:
        if 1<=day<=30:
            pass
        else:
            ans=-1
    elif month==2:
        if 1<=day<=29:
            pass
        else:
            ans=-1
    else:
        ans=-1
    if ans==-1:
        print(f"#{i+1} -1")
    else:
        print(f"#{i+1} {year:04d}/{month:02d}/{day:02d}")