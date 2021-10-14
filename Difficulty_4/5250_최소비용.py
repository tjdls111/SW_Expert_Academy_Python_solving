# import sys
#
# sys.stdin = open('11782.txt')

import heapq


def dijkstra():
    while q:
        # 가장 짧은 거리 찾기
        v_dis, vi, vj = heapq.heappop(q)

        if visited[vi][vj]:  # 방문했던 아이가 들어가면
            continue

        visited[vi][vj] = True

        # 거기에서 인접하고(4방향) 방문 안한 정점들의 거리 업데이트
        for k in range(4):
            ni = vi + directions[k][0]
            nj = vj + directions[k][1]

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == False:  # 범위, 방문 체크
                height_difference = arr[ni][nj] - arr[vi][vj] # 더 높은 곳으로 이동하면 높이 차이만큼 연료 추가 소비
                if height_difference > 0:
                    fuel_cost[ni][nj] = min(fuel_cost[ni][nj], fuel_cost[vi][vj] + 1 + height_difference)
                else:
                    fuel_cost[ni][nj] = min(fuel_cost[ni][nj], fuel_cost[vi][vj] + 1)
                heapq.heappush(q, (fuel_cost[ni][nj], ni, nj))


directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

MIIS = lambda: map(int, input().strip().split())
INF = 1000000 * 1000

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(list(MIIS()) for _ in range(N))

    visited = [[0] * N for _ in range(N)]
    fuel_cost = [[INF] * N for _ in range(N)]

    q = []
    fuel_cost[0][0] = 0
    q.append((fuel_cost[0][0], 0, 0))

    dijkstra()

    print(f'#{tc} {fuel_cost[N - 1][N - 1]}')
