t=int(input())

for i in range(t):
    n=input()
    for j in range(1,len(n)):
        if n[:j]==n[j:2*j]:
            #print("answer!"+n[:j])
            break

    print(f"#{i+1} {len(n[:j])}")