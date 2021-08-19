# 파스칼의 삼각형 - 이항계수 - 조합이다.
# 조합 O(2^n)..
# DP를 해야 한다.
memo = [[0] * (10+1) for _ in range(10+1)]

T = int(input())
for tc in range(1,T+1):
    N =int(input())