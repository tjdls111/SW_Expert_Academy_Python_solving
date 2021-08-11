# 1954. 달팽이 숫자
# import sys
# sys.stdin = open("1954_input.txt")

T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    arr = list([0] * N for _ in range(N))

    cnt = 1
    long = N
    long_cnt = 0
    mode = 0
    i, j = 0, -1
    while long >= 0 :
        ni = i + di[mode]
        nj = j + dj[mode]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0 and long_cnt <= long:
            arr[ni][nj] = cnt
            cnt += 1
            long_cnt += 1
            i, j = ni, nj
        else:
            if mode == 1 or mode == 3:
                long -= 1
            mode = (mode + 1) % 4
            long_cnt = 0


    # 출력
    print("#{}".format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()

