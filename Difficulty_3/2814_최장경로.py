# import sys
#
# sys.stdin = open('2814.txt')

ans = 0
T = int(input())


def dfs(v, cnt):
    global ans

    for w in adj[v]:
        if visited[w] == False:
            visited[w] = True
            dfs(w, cnt + 1)
            visited[w] = False
    ans = max(ans, cnt)


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    visited = [False] * (N + 1)
    ans = 0

    for i in range(1, N + 1):
        visited[i] = True
        dfs(i, 1)
        visited[i] = False
    print(f'#{tc} {ans}')
