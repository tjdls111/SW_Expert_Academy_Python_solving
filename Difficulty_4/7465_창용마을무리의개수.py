# 서로소 집합
import sys

sys.stdin = open('7465.txt')


def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])


def union(x, y):
    parent[find_set(x)] = parent[find_set(y)]


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 일단 각각 혼자만 알고 있다고 만들기
    parent = [0] + list(range(1, N + 1))

    # 신청서 낸 친구들을 같은 조로 만들기
    for _ in range(M):
        people1, people2 = map(int, input().split())
        union(people1, people2)

    # 무리 개수
    cnt = 0
    for i in range(1, N + 1):
        if find_set(i) == i:
            cnt += 1

    print(f'#{tc} {cnt}')
