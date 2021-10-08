# import sys
#
# sys.stdin = open('1861.txt')

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))
    visit = [0] * (N ** 2 + 1)
    # 다음 방 갈 수 있는지 체크
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + directions[k][0]
                nj = j + directions[k][1]
                if 0 <= ni < N and 0 <= nj < N:
                    if arr[ni][nj] == arr[i][j] + 1:
                        visit[arr[i][j]] = 1
                        continue

    # 방문 가능하다고 연속 체크된 것 최대 개수 세기
    ans_start_idx = 0
    ans_max_num = 0
    
    tmp_max_num = 1
    start_room_num = 0
    flag = False
    for i in range(N * N + 1):
        if visit[i] == 1:
            if flag == False:
                flag = True
                start_room_num = i
            tmp_max_num += 1
        else:
            flag = False
            if ans_max_num < tmp_max_num:
                ans_max_num = tmp_max_num
                ans_start_idx = start_room_num
            
            tmp_max_num = 1
    print(f'#{tc} {ans_start_idx} {ans_max_num}')
