import sys

sys.stdin = open('1244_input.txt')


def change(n, k):
    global max_num

    for i in range(len(arr[change_cnt])):
        tmp_arr = list(str(arr[change_cnt][i]))

        for j in range(n):
            for kk in range(j+1, n):
                tmp_arr[j], tmp_arr[kk] = tmp_arr[kk], tmp_arr[j]

                if ''.join(tmp_arr) not in arr[change_cnt + 1]:
                    arr[change_cnt + 1].append(''.join(tmp_arr))

                if change_cnt == (cnt - 1):
                    max_num = max(max_num, int(''.join(tmp_arr)))
                    
                tmp_arr[j], tmp_arr[kk] = tmp_arr[kk], tmp_arr[j] # 원상복구

T = int(input())

for tc in range(1, T + 1):
    num, cnt = map(int, input().split())
    num_list = list(str(num))

    arr = list([] for _ in range(cnt + 1))
    arr[0] = [str(num)]

    max_num = 0
    change_cnt = 0

    while change_cnt < cnt:
        change(len(num_list), 0)
        change_cnt += 1

    print('#{} {}'.format(tc, max_num))
    # print(arr)
