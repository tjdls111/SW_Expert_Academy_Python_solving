# import sys
# sys.stdin = open('1247_input.txt')

def dfs(curr_city, total_cost):
    global smallest_cost

    if total_cost >= smallest_cost: # 이동 거리가 지금 최소값보다 크면 정답으로 가망 없으니 리턴
        return

    if curr_city == 1: # 집 도착
        for v in visited:
            if v == False: # 고객들 중 방문 안한 곳 있으면
                return
        smallest_cost = min(smallest_cost, total_cost)
        return

    for i in range(N+2):
        next_city_cost = distance[curr_city][i]
        if visited[i] == False: # 제자리 아니고, 방문 안한 곳이라면
            visited[i] = True
            dfs(i, total_cost + next_city_cost)
            visited[i] = False


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    location= [] # 회사, 집, 고객들의 좌표
    for i in range(N+2):
        location.append((arr[i*2], arr[i*2+1]))

    # 각 이동 거리 계산
    distance = [[0] * (N+2) for _ in range(N+2)]
    for i in range(N+2):
        for j in range(i+1, N+2):
            tmp = abs(location[i][0] - location[j][0] ) + abs(location[i][1] - location[j][1])
            distance[i][j] = tmp
            distance[j][i] = tmp

    visited = [False] * (N+2) # 도시 방문 체크
    smallest_cost = 100*100*13
    # 회사에서부터 출발
    visited[0] = True
    dfs(0, 0) # 출발 도시, 이동 거리
    print('#{} {}'.format(tc, smallest_cost))


