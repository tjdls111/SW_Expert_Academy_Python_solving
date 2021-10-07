# import sys
#
# sys.stdin = open('1865.txt')

def dfs(depth, total):
    global ans

    if ans >= total:
        return

    if depth == N:
        ans = max(ans, total)
        return

    for i in range(N):
        if check[i] == False:  # 방문 안 한 곳
            tmp = success_chance[depth][i]*(0.01)
            if tmp >= ans:
                check[i] = True
                dfs(depth + 1, total * tmp)
                check[i] = False

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    success_chance = tuple(tuple(map(int, input().split())) for _ in range(N))

    ans = 0
    check = [False] * N
    dfs(0, 1)
    ans *= 100
    print('#%d %.6f' %(tc, ans))
