import heapq
# import sys
#
# sys.stdin = open('11783.txt')


def dijkstra():
    while q:
        # 가장 짧은 거리 찾기
        v_dis, v = heapq.heappop(q)

        if visited[v]: # 방문했던 아이가 들어가면
            continue

        visited[v] = True


        # 거기에서 인접하고 방문 안한 정점들의 거리 업데이트
        for w in range(N + 1):
            if adj[v][w] > 0 and not visited[w]:
                distance[w] = min(distance[w], distance[v] + adj[v][w])
                heapq.heappush(q, (distance[w], w))


T = int(input())

MIIS = lambda: map(int, input().strip().split())
INF = 1000000 * 1000

for tc in range(1, T + 1):
    N, E = MIIS()

    adj = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [False] * (N + 1)
    distance = [INF] * (N + 1)

    for _ in range(E):
        s, e, w = MIIS()
        adj[s][e] = w

    q = []
    start = 0
    distance[start] = 0
    heapq.heappush(q, (0, distance[start]))
    dijkstra()
    print(f'#{tc} {distance[N]}')
