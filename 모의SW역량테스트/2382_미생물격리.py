# import sys
import copy
# sys.stdin = open("../input.txt")

T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split())

    # 미생물 군집 정보 저장 & 초기화
    microbes = []
    for _ in range(K):
        col, row, cnt, direct = map(int,input().split())
        microbes.append([col, row, cnt, direct])

    # M 시간 동안
    for t in range(M):
        # 미생물 쭉 보면서
        for i in range(len(microbes)):
            col, row, cnt, direct = microbes[i]
            # 이동 시키기
            if direct == 1: # 상
                microbes[i] = [col-1, row, cnt, direct]
            elif direct==2: # 하
                microbes[i] = [col+1, row, cnt, direct]
            elif direct==3: # 좌
                microbes[i] = [col, row-1, cnt, direct]
            elif direct==4: # 우
                microbes[i] = [col, row+1, cnt, direct]

        # 미생물 쭉~ 보면서
        new_microbes = []
        for i in range(len(microbes)):
            col, row, cnt, direct = microbes[i]

            # 약품 부분으로 가면 (방향- 반대로, 수 - 절반)
            if col == 0 or col == N-1 or row == 0 or row == N-1:
                cnt = int(cnt/2) # 수 절반
                if cnt == 0:
                    # 만약에 0이면 군집 없애기
                    pass
                else:
                    # 방향 반대로
                    if direct == 1 or direct==3:
                        direct += 1
                    elif direct == 2 or direct == 4:
                        direct -= 1
                    new_microbes.append([col, row, cnt, direct])
            else:
                new_microbes.append([col, row, cnt, direct])
        microbes = copy.deepcopy(new_microbes)

        # 미생물 정렬(같은 위치인지 편하게 보려고)
        microbes.sort()
        # 만나면(방향 - 가장 큰 군집 방향으로, 수 - 다 더하기)
        new_microbes = []
        idx = 0
        cnt_total = 0
        direct=[-1,-1]
        flag = False

        while idx < len(microbes)-1:
            cnt_total = microbes[idx][2]
            direct = (microbes[idx][3], microbes[idx][2]) # 방향, 수

            while True and idx < len(microbes)-1:
                if microbes[idx][0] == microbes[idx+1][0] and microbes[idx][1] == microbes[idx+1][1]: # 같은 좌표에 여러 군집
                    cnt_total += (microbes[idx+1][2])
                    if direct[1] < microbes[idx+1][2]:
                        direct = (microbes[idx+1][3], microbes[idx+1][2])
                    idx += 1
                    flag = True
                else:
                    new_microbes.append([microbes[idx][0], microbes[idx][1], cnt_total, direct[0]])
                    idx += 1
                    flag = False
                    break
        # 마지막 꺼 반영
        if flag == False:
            new_microbes.append([microbes[idx][0], microbes[idx][1], microbes[idx][2], microbes[idx][3]])
        else:
            new_microbes.append([microbes[idx][0], microbes[idx][1], cnt_total, direct[0]])

        microbes = copy.deepcopy(new_microbes)
    # print([c for a, b, c, d in microbes])
    print(f'#{tc} {sum([c for a, b, c, d in microbes])}')
