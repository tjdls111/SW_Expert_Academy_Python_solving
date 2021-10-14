# import sys
#
# sys.stdin = open('11775.txt')
#

def dfs(depth, total):
    global ans

    if ans <= total:
        return

    if depth == N:
        ans = min(ans, total)
        return

    for i in range(N):
        if check[i] == False:  # 방문 안 한 곳
            tmp = production_expenses[depth][i]
            if tmp < ans:
                check[i] = True
                dfs(depth + 1, total + tmp)
                check[i] = False

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    production_expenses = tuple(tuple(map(int, input().split())) for _ in range(N))

    ans = 987654321
    check = [False] * N
    dfs(0, 0)
    print(f'#{tc} {ans}')
