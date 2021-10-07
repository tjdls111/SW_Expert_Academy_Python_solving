import sys

sys.stdin = open('11772.txt')


def binary_search(l, r, target):
    global check
    if l > r:
        return False

    mid = (l + r) // 2
    mid_value = A[mid]

    if target == mid_value:
        return True

    elif target < mid_value:
        if check == 'L':
            return False
        check = 'L'
        return binary_search(l, mid - 1, target)

    elif target > mid_value:
        if check == 'R':
            return False
        check = 'R'
        return binary_search(mid + 1, r, target)


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    ans = 0
    for b in B:
        check = 0
        if binary_search(0, N - 1, b) == True:
            ans += 1

    print(f'#{tc} {ans}')
