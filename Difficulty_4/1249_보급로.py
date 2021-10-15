import heapq
import sys

sys.stdin = open('1249.txt')


def dijkstra(starti, startj):
    visited = [[False] * N for _ in range(N)]


    Q = []
    # 출발점에서 출발점으로 갈 때 비용은 0, 그때 좌표
    cost[starti][startj]= 0
    heapq.heappush(Q, (cost[starti][startj], starti, startj))

    while Q:
        curr_cost, i, j = heapq.heappop(Q)  # 지금 인접한 것 중에서 가장 비용 적게 드는 것..

        if visited[i][j]: # 방문했던 거면 X
            continue

        visited[i][j] = True # 방문 체크

        if i == N - 1 and j == N - 1: # 정답 찾았으면 리턴
            return cost[i][j]


        for k in range(4): # 인접한 것드
            # 인접하는 것 비용 업데이트할 수 있으면 하기
            ni = i + directions[k][0]
            nj = j + directions[k][1]

            # 범위, 방문체크
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                cost[ni][nj] = min(cost[ni][nj], curr_cost + arr[ni][nj])

                heapq.heappush(Q, (cost[ni][nj], ni, nj))


T = int(input())
INF = 98765432198765
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
for tc in range(1, T + 1):
    N = int(input())
    arr = list(list(map(int, input())) for _ in range(N))
    cost = [[INF] * N for _ in range(N)]

    # 다익스트라
    print(f'#{tc} {dijkstra(0,0)}')

    # print(cost[N-1][N-1])