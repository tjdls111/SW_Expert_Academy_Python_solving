# import sys
#
# sys.stdin = open('1486.txt')
#

def powerset(idx, curr_total, left_people_sum):
    global ans
    if idx > N:
        return

    if curr_total >= ans:  # 현재 답보다, 키의 합이 크거나 같으면
        return

    if left_people_sum + curr_total < B:  # 남은 걸로는 목표치 달성 불가
        return

    if curr_total >= B:
        ans = min(ans, curr_total)
        return

    powerset(idx + 1, curr_total, left_people_sum - arr[idx])  # 점원 안 쓰는 경우
    powerset(idx + 1, curr_total + arr[idx], left_people_sum - arr[idx])  # 점원 쓰는 경우


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 10000 * 20 + 1

    powerset(0, 0, sum(arr))
    print(f'#{tc} {abs(ans - B)}')
