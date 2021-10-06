# import sys
#
# sys.stdin = open('2819.txt')


def dfs(curr: tuple, cnt: int, num: str):  # 현재 위치, 몇번째인지, 그때까지 숫자 이어붙인 것
    if cnt == 7:
        ans.add(num)
        return

    curr_i, curr_j = curr
    for k in range(4):
        ni = curr_i + directions[k][0]
        nj = curr_j + directions[k][1]

        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs((ni, nj), cnt + 1, num + str(arr[ni][nj]))


# 상하좌우
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
T = int(input())
for tc in range(1, T + 1):
    arr = list(list(map(int, input().strip().split())) for _ in range(4))

    ans = set()
    for i in range(4):
        for j in range(4):
            # 격자판의 모든 위치에서 시작
            dfs((i, j), 0, '')
    print(f'#{tc} {len(ans)}')
