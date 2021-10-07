import sys

sys.stdin = open('11772.txt')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    ans = 0
    for b in B:
        l = 0
        r = N - 1
        check = 0
        while l <= r:
            mid = (l + r) // 2
            mid_value = A[mid]
            if b == mid_value:
                ans += 1
                break
            elif b < mid_value:
                r = mid - 1
                if check == 'L':
                    break
                else:
                    check = 'L'

            elif b > mid_value:
                l = mid + 1
                if check == 'R':
                    break
                else:
                    check = 'R'
    print(f'#{tc} {ans}')
