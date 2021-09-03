# import sys
#
# sys.stdin = open('input.txt')

# 오른쪽, 아래쪽, 아랫쪽 대각선 두개만 보기
directions = [(0, 1), (1, 0), (1, 1), (1, -1)]


def sol():
    for i in range(N):  # 쭉 보면서 (왼->오, 위-> 아래 순서)
        for j in range(N):
            if board[i][j] == 'o':
                for k in range(4):
                    ni = i + directions[k][0]
                    nj = j + directions[k][1]

                    if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 'o':  # 돌이 있으면
                        cnt = 1
                        nni, nnj = ni, nj
                        while 0 <= nni < N and 0 <= nnj < N and board[nni][nnj] == 'o':  # 그 방향으로 쭉~~
                            cnt += 1
                            nni += directions[k][0]
                            nnj += directions[k][1]
                            if cnt == 5:  # 다섯개이면 정답
                                return 'YES'
    return 'NO'


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = list(list(input()) for _ in range(N))
    print('#{} {}'.format(tc,sol()))
