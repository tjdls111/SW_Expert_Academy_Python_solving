import sys

sys.stdin = open("../input.txt")

T= int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(input())

    one_number_length = N//4

    numbers = set() # 중복 없애려고 set

    # spinning_cnt만큼 회전시키기
    for i in range(one_number_length):


        for j in range(1, 5): # 4번 반복
            # one_number_length만큼 끊어서 numbers에 넣기
            tmp = ''.join(arr[one_number_length*(j-1):one_number_length*j])

            numbers.add(tmp)

        # 한칸 시계방향 순으로 회전
        tmp = arr.pop()
        arr.insert(0, tmp)

    # 생성 가능한 수를 내림차순 정렬
    numbers = sorted(list(numbers), reverse=True)

    # K번째 수
    ans_hex = numbers[K-1].lower()

    # 16진수 -> 10진수
    print(f'#{tc} {int(ans_hex, 16)}')
