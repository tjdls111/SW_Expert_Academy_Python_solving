import collections
# import sys
#
# sys.stdin = open('11779.txt')

T = int(input())


def bfs(num):
    global ans

    q = collections.deque()
    q.append((num, 0))

    while q:
        tmp_num, tmp_cnt = q.popleft()

        if tmp_num == target:
            ans = min(ans, tmp_cnt)
            return

        candidates = [tmp_num+1, tmp_num-1, tmp_num*2, tmp_num-10]
        for candidate in candidates:
            if candidate not in visited and candidate > 0 and candidate <= 1000000:
                visited.add(candidate)
                q.append((candidate, tmp_cnt + 1))



for tc in range(1, T + 1):
    first_num, target = map(int, input().split())

    visited = set()
    ans = 987654321

    bfs(first_num)
    print(f'#{tc} {ans}')
