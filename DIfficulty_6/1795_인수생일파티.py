# 간선 정보 원래 방향대로 받아서 -> X에서 출발해서 다른 곳 도착하는 비용 계산
# 간선 정보 반대 방향으로 받아서 -> X에서 출발해서 다른 곳 도착하는 비용 계산.

import heapq
import sys

sys.stdin = open('1795.txt')


def dijikstra(start, abj):
    # 비용 담긴 리스트
    cost = [987654321] * (V + 1)
    visited = [False] * (V + 1)

    # 출발점 초기화
    Q = []
    heapq.heappush(Q, (0, start))  # 출발점에서 어떤 집까지 가는 데 드는 비용, 그 집 번호

    while Q:
        curr_cost, curr_house = heapq.heappop(Q)
        if visited[curr_house]:
            continue
        visited[curr_house] = True
        cost[curr_house] = curr_cost
        # 그 집 근처 비용 업데이트
        for i in range(1, V + 1):
            if visited[i] == False:  # 방문 안 했으면
                cost[i] = min(cost[i], cost[curr_house] + abj[curr_house][i])
                heapq.heappush(Q, (cost[i], i))
    return cost


T = int(input())

for tc in range(1, T + 1):
    V, E, insu_house = map(int, input().split())
    origin_abj = [[987654312] * (V + 1) for _ in range(V + 1)]
    opposite_abj = [[987654321] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        s, e, cost = map(int, input().split())
        origin_abj[s][e] = cost
        opposite_abj[e][s] = cost

    # 자기 위치 0으로
    for i in range(V+1):
        origin_abj[i][i] = 0
        opposite_abj[i][i] = 0

    origin_res = dijikstra(insu_house, origin_abj)
    oppo_res = dijikstra(insu_house, opposite_abj)

    # 계산
    ans  = 0
    for i in range(1,V+1):
        ans = max(ans, origin_res[i] + oppo_res[i])

    print(f'#{tc} {ans}')
