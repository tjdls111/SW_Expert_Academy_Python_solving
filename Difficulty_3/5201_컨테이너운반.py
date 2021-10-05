# import sys
#
# sys.stdin = open('11764.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    cargo_weights = list(map(int, input().split()))
    truck_capacities = list(map(int, input().split()))

    # 컨테이너, 트럭 무거운 순서대로 정렬
    cargo_weights.sort(reverse=True)
    truck_capacities.sort(reverse=True)

    ans = 0
    for cw in cargo_weights:  # 컨테이너를 무거운 순서대로 보면서
        for tc in truck_capacities:
            if cw > tc:  # 트럭이 못 나르면 break(그 이후에는 그것보다 더 싣는 트럭 없음)
                break
            else:  # 트럭이 그것 나를 수 있으면 나르게 하기
                ans += cw
                truck_capacities.remove(tc)
                break
    print(f'#{test_case} {ans}')
