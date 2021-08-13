# 1221. [S/W 문제해결 기본] 5일차 - GNS
# import sys
#
# sys.stdin = open("1221.GNS_input.txt")

T = int(input())
for tc in range(1, T + 1):
    _ = input()
    arr = list(input().split())

        # 문자 -> 숫자
    for i in range(len(arr)):
        if arr[i] == "ZRO":
            arr[i] = 0
        elif arr[i] == "ONE":
            arr[i] = 1
        elif arr[i] == "TWO":
            arr[i] = 2
        elif arr[i] == "THR":
            arr[i] = 3
        elif arr[i] == "FOR":
            arr[i] = 4
        elif arr[i] == "FIV":
            arr[i] = 5
        elif arr[i] == "SIX":
            arr[i] = 6
        elif arr[i] == "SVN":
            arr[i] = 7
        elif arr[i] == "EGT":
            arr[i] = 8
        elif arr[i] == "NIN":
            arr[i] = 9

    # 정렬
    cnt_arr = [0]*10

    for i in range(len(arr)):
        cnt_arr[arr[i]] += 1

    # 숫자 -> 문자 바로 출력
    print("#{}".format(tc))
    for i in range(10):
        if i == 0:
            print("ZRO "*cnt_arr[i])
        elif i == 1:
            print("ONE "*cnt_arr[i])
        elif i == 2:
            print("TWO " * cnt_arr[i])
        elif i == 3:
            print("THR " * cnt_arr[i])
        elif i == 4:
            print("FOR " * cnt_arr[i])
        elif i == 5:
            print("FIV " * cnt_arr[i])
        elif i == 6:
            print("SIX " * cnt_arr[i])
        elif i == 7:
            print("SVN " * cnt_arr[i])
        elif i == 8:
            print("EGT " * cnt_arr[i])
        elif i == 9:
            print("NIN " * cnt_arr[i])

