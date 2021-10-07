import sys

sys.stdin = open('11773.txt')


def dfs(left_battery, change_cnt, curr_idx):
    global ans

    if ans <= change_cnt: # 가지치기
        return

    if curr_idx == N - 2:
        if left_battery >= 1:  # 도착했으면
            ans = min(ans, change_cnt)
        return

    if left_battery > 0:  # 충전 안해도 될 때
        dfs(left_battery - 1, change_cnt, curr_idx + 1)
    dfs(arr[curr_idx]-1, change_cnt + 1, curr_idx + 1)


T = int(input())

for tc in range(1, T + 1):
    tmp = list(input().split())
    N = int(tmp[0])
    arr = list(map(int, tmp[1:]))
    ans = 100 * 100 + 1
    dfs(arr[0]-1, 0, 1)
    print(f'#{tc} {ans}')
