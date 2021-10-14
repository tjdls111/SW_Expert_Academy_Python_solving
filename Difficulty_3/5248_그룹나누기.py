# 서로소 집합
# import sys
#
# sys.stdin = open('11780.txt')

def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])

def union(x, y):
    parent[find_set(x)]  = parent[find_set(y)]

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    applications = list(map(int, input().split()))

    # 각각 혼자서 조로 만들기
    parent = [0] + list(range(1,N+1))

    # 신청서 낸 친구들을 같은 조로 만들기
    for i in range(M):
        applicant, respondent = applications[i*2], applications[i*2+1]
        union(applicant, respondent)

    # 다른 조가 몇 개인지
    cnt = 0
    for i in range(1, N+1):
        if find_set(i) == i:
            cnt += 1

    print(f'#{tc} {cnt}')