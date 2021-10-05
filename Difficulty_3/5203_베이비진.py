# import sys
#
# sys.stdin = open('11767.txt')


def check_babygin(num: str):
    if num[0] == num[1] and num[1] == num[2]:
        return 'triplet'
    elif int(num[0]) + 1 == int(num[1]) and int(num[1]) + 1 == int(num[2]):
        return 'run'
    return False


def perm(n, r, k):  # 원소의 개수, 몇 개 뽑는지, 깊이
    if k == r:
        answer_candidates.append(''.join(map(str, p)))
    else:
        for i in range(n):
            if used[i] == 0:
                p[k] = list(range(n))[i]
                used[i] = 1  # 사용 체크
                perm(n, r, k + 1)
                used[i] = 0  # 원상복구


T = int(input())
for tc in range(1, T + 1):
    arr = list(input().split())

    player1 = []
    player2 = []

    for i in range(6):
        player1.append(arr[i * 2])
        player2.append(arr[i * 2 + 1])

    # 카드 3장일 때~ 6장일 때 쭉 보면서 언제 가장 먼저 run이나 triplet이 되는지
    for i in range(3, 7):
        # 지금 가진 패 (순서대로)
        player1_have = player1[:i + 1]
        player2_have = player2[:i + 1]

        # 3장씩 뽑아보면서
        p = [0] * 3
        used = [0] * i
        answer_candidates = []  # 3장씩 뽑는 경우들
        perm(i, 3, 0)

        # player1, 2가 run이나 triplet이 되었는지 보기
        for answer_candidate in answer_candidates:
            player1_tmp = player1_have[int(answer_candidate[0])] + player1_have[int(answer_candidate[1])] + \
                          player1_have[int(answer_candidate[2])]
            player2_tmp = player2_have[int(answer_candidate[0])] + player2_have[int(answer_candidate[1])] + \
                          player2_have[int(answer_candidate[2])]

            if check_babygin(player1_tmp):
                ans = 1
                break
            elif check_babygin(player2_tmp):
                ans = 2
                break
        else:
            ans = 0

    print(f'#{tc} {ans}')
