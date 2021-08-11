# 1209. [S/W 문제해결 기본] 2일차 - Sum
# import sys
# sys.stdin = open("1209_input.txt")

for _ in range(10):
    tc = int(input())
    arr = list(list(map(int,input().split())) for _ in range(100))

    max_sum = 0
    # 각 행의 합(가로들)
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[i][j]
        if sum > max_sum:
            max_sum = sum

    # 각 열의 합(세로들)
    for j in range(100):
        sum = 0
        for i in range(100):
            sum += arr[i][j]
        if sum > max_sum:
            max_sum = sum

    # 대각선
    sum = 0
    sum1 = 0
    sum2 = 0
    for i in range(100):
        sum1 += arr[i][i]
        sum2 += arr[i][99-i]

    if sum1 > sum2:
        sum = sum1
    else:
        sum = sum2

    if sum > max_sum:
        max_sum = sum

    print("#{} {}".format(tc, max_sum))





