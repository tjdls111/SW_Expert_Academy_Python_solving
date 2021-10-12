import collections
# import sys
#
# sys.stdin = open('5656.txt')

import copy


def perm(k):  # 원소의 개수, 깊이
    if k == N:
        candidates.append(p[::])

    else:
        for i in range(W):
            p[k] = arr2[i]
            perm(k + 1)  # 하나 더 깊숙이 가서


def break_bricks(ii, jj, power):
    # 일단 그 벽돌 깨기
    tmp_arr[ii][jj] = 0

    # 주변 벽돌 깨기
    for i in range(1, power):
        for j in range(1, power):
            for x in range(4):
                ni = ii + directions[x][0] * i
                nj = jj + directions[x][1] * j

                if 0 <= ni < H and 0 <= nj < W:
                    if tmp_arr[ni][nj] > 1:  # 범위 체크, 또 다른 벽돌 깰 수 있으면
                        q.append((ni, nj, tmp_arr[ni][nj]))  # 큐에 넣기
                    # 깨뜨리기
                    tmp_arr[ni][nj] = 0


def move():
    for j in range(W):
        blank = H - 1
        brick = H - 1
        while blank >= 0 and brick >= 0:
            if tmp_arr[blank][j] == 0:
                while brick >= 0 and tmp_arr[brick][j] == 0:
                    brick -= 1
                if blank > brick and brick != -1:
                    tmp_arr[blank][j], tmp_arr[brick][j] = tmp_arr[brick][j], tmp_arr[blank][j]
                else:
                    brick -= 1
            else:
                blank -= 1


def dfs(garo, k):  # 어느 위치의 벽돌을 깰 것인지, 몇 번 구슬을 쏘았는지
    global ans
    if k == N + 1:
        brick_total = 0
        for i in range(H):
            for j in range(W):
                if tmp_arr[i][j] > 0:
                    brick_total += 1
        ans = min(ans, brick_total)
        return

    for kk in range(H):
        if tmp_arr[kk][garo] > 0:  # 벽돌이 있으면
            break_bricks(kk, garo, tmp_arr[kk][garo])
            break

    while q:
        i, j, power = q.popleft()
        break_bricks(i, j, power)

    # 내려주기
    move()

    dfs(c[k], k + 1)


# 4방향
MIIS = lambda: map(int, input().strip().split())
directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
T = int(input().strip())
for tc in range(1, T + 1):
    N, W, H = MIIS()
    arr = list(list(MIIS()) for _ in range(H))
    ans = 98765432198

    candidates = []

    arr2 = range(W)
    p = [0] * (N+1)  # 중복순열
    perm(0)

    for c in candidates:
        q = collections.deque()
        tmp_arr = copy.deepcopy(arr)
        dfs(c[0], 1)
        if ans == 0:
            break
    print(f'#{tc} {ans}')
