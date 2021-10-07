# import sys
#
# sys.stdin = open('11770.txt')


def partition(A: list, l, r):
    p = A[l] # 피벗 값
    i = l
    j = r
    while i < j:
        while i < r and A[i] <= p: # 피벗보다 큰 값 찾으면 멈춤
            i += 1
        while l < j and A[j] >= p: # 피벗보다 작은 값 찾으면 멈춤
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]

    A[l], A[j] = A[j], A[l] # 피벗을 가운데에 놓기
    return j


def quickSort(A: list, l, r):
    if l < r:
        s = partition(A, l, r)
        quickSort(A, l, s - 1)
        quickSort(A, s + 1, r)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    quickSort(arr, 0, N-1)
    print(f'#{tc} {arr[N//2]}')
