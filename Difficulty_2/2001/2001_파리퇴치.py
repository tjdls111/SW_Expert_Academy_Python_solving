# 2001. 파리 퇴치
# import sys
#
# sys.stdin = open("../2001_파리퇴치_input.txt")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))

    max_val = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            cnt = 0
            for ii in range(i, i+M):
                for jj in range(j, j+M):
                    cnt += arr[ii][jj]

            if max_val < cnt:
                max_val = cnt

    print("#{} {}".format(tc, max_val))
