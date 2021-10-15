import sys

sys.stdin = open('1251.txt')

import heapq


def dis_calc(x, y):
    i1 = xs[x]
    i2 = xs[y]

    j1 = ys[x]
    j2 = ys[y]
    #
    # if i1 == i2 and j1 != j2:
    #     return (j1 - j2) ** 2
    #
    # if i1 != i2 and j1 == j2:
    #     return (i1 - i2) ** 2
    #
    # if i1 != i2 and j1 != j2:
    return (i1 - i2) ** 2 + (j1 - j2) ** 2


def prim():
    visited = [False] * N
    Q = []

    heapq.heappush(Q, (0, 0))  # 0에서 출발

    ans = 0

    while Q:
        curr_cost, curr_island = heapq.heappop(Q)  # 가장 작은 정점 가져옴

        if visited[curr_island]:
            continue

        ans += curr_cost
        visited[curr_island] = True
        cost[curr_island] = curr_cost

        # 비용 업데이트
        for i in range(N):
            if islands[curr_island][i] != INF and not visited[i]:  # 인접이고 방문 안했으면
                cost[i] = min(cost[i], islands[curr_island][i])
                heapq.heappush(Q, (cost[i], i))
    return ans

INF = 0xffffffffff
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    islands = [[INF] * N for _ in range(N)]
    cost = [INF] * N
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    E = float(input())

    for i in range(N):
        for j in range(i+1, N):
            # 방향이 없다
            islands[j][i] = islands[i][j] = min(islands[i][j], dis_calc(i, j))

    for i in range(N):
        islands[i][i] = 0

    ans = prim()
    print(f'#{tc} {int(sum(cost) * E + 0.5)}')
    # print(f'#{tc} {int(ans * E + 0.5)}')
