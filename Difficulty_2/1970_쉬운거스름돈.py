# import sys
#
# sys.stdin = open('1970.txt')

money_type = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())
for tc in range(1, T + 1):
    n = int(input())

    print(f'#{tc}')
    for i in range(8):
        cnt = n // money_type[i]
        n -= (money_type[i] * cnt)

        print(cnt, end=' ')
    print()
