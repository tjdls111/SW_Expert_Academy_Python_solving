import sys

sys.stdin = open('2105.txt')

# 대각선 방향
directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


def dfs(i, j, direction_type, dessert_cnt):
    global ans

    # 직진 or 꺾기
    if direction_type < 3:
        tmp = direction_type + 2
    else:
        tmp = direction_type + 1

    for k in range(direction_type, tmp):
        ni = i + directions[k][0]
        nj = j + directions[k][1]

        if start[0] == ni and start[1] == nj:  # 왔던 곳으로 돌아옴
            ans = max(ans, dessert_cnt)
            return

        # 범위 벗어나면 X
        if 0 <= ni < N and 0 <= nj < N:
            if cafe_visited[ni][nj] == False and dessert_visited[arr[ni][nj]] == False:  # 방문하지 않은 카페 & 먹지 않은 디저트

                cafe_visited[ni][nj] = True
                dessert_visited[arr[ni][nj]] = True

                dfs(ni, nj, k, dessert_cnt + 1)

                cafe_visited[ni][nj] = False
                dessert_visited[arr[ni][nj]] = False


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))

    cafe_visited = [[False] * N for _ in range(N)]
    dessert_visited = [False] * 101
    ans = -1

    # 사각형 모양을 그리며 출발하고 카페로 돌아와야 함.

    for i in range(N):
        for j in range(N):
            start = (i, j)
            cafe_visited[i][j] = True
            dessert_visited[arr[i][j]] = True

            dfs(i, j, 0, 1)

            cafe_visited[i][j] = False
            dessert_visited[arr[i][j]] = False

    print(f'#{tc} {ans}')