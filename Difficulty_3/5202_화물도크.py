# import sys
#
# sys.stdin = open('13089.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    applications = [tuple(map(int, input().split())) for _ in range(N)]

    # 끝나는 시각이 빠른 순서대로 정렬 (끝나는 시각이 같으면 시작 시간이 빠르게..)
    applications.sort(key=lambda x: (x[1], x[0]))

    ans = 1
    finish_time = applications[0][1]

    for i in range(1, N):
        if finish_time <= applications[i][0]:
            ans += 1
            finish_time = applications[i][1]
    print(f'#{tc} {ans}')