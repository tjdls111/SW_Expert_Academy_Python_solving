from typing import no_type_check


T = int(input())
for i in range(T):
    n = int(input())
    dy = [[] for _ in range(n)]
    dy[0] = [1]

    #print(dy)

    for i in range(1,n):
        dy[i].append(1)
        
        for j in range(1, i):
            dy[i].append(dy[i-1][j-1] + dy[i-1][j])
        dy[i].append(1)

    print(f'#{i+1}')
    for d in dy:
        for i in d:
            print(i,end=' ')
        print()