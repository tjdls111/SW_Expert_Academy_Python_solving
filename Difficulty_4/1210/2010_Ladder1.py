# 1210. [S/W 문제해결 기본] 2일차 - Ladder1
# 도착점(X)부터 위로 올라가서 출발점 찾기
import sys

sys.stdin = open("2010_Ladder1_input.txt")

# 좌, 우, 상 (상이 가장 마지막에 있어야 함)
mode = [[0, -1], [0, 1], [-1, 0]]


def sol(i, j):
    # 거기에서부터 위나 옆으로 길이 있으면 쭉 가다가,
    # 맨 위까지 오면 거기의 위치를 반환하는 함수

    arr[i][j] = -1
    while True:
        # 상, 좌, 우 길이 있는지 체크
        for m in range(3):
            ni = i + mode[m][0]
            nj = j + mode[m][1]
            if 0 <= ni < 100 and 0 <= nj < 100 and arr[ni][nj] == 1:
                # 갔던 곳은 다시 못가게 -1로 바꿔버리기!
                arr[i][j] = -1
                i = ni
                j = nj
                if i == 0:
                    return nj


T = 10
for tc in range(1, T + 1):
    testcase = input()
    arr = list(list(map(int, input().split())) for _ in range(100))
    # print(arr)

    # 맨 아래에서 도착점 찾기
    finish_idx_j = -1
    for n in range(100):
        if arr[99][n] == 2:
            finish_idx_j = n
            # print(finish_idx_j)
            print("#{} {}".format(tc,sol(99, finish_idx_j)))
            break
