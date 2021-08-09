# 1206. [S/W 문제해결 기본] 1일차 - View

# import sys
# sys.stdin = open("1206_input.txt")

for i in range(1, 11):
    # 입력 받기
    n = int(input())
    houses = list(map(int,input().split()))

    have_prospect_right = 0  # 조망권 있는 세대 수

    # 각 아파트를 보면서 조망권 있는 세대 수 보기
    for j in range(2, n-2):
        min_cnt = 256  # 각 빌딩의 최대 높이는 255이므로
        for k in [-2, -1, 1, 2]:  # 좌, 우 두 건물씩 살펴봄
            if houses[j]-houses[j + k] <= 0:  # 좌우 건물이 더 높거나 같으면 break
                break
            min_cnt = min(houses[j]-houses[j + k], min_cnt)
        else:  # break되지 않았으면 즉, 좌우 건물보다 해당 건물이 더 높으면
            have_prospect_right += min_cnt

    # 출력
    print("#{} {}".format(i, have_prospect_right))



