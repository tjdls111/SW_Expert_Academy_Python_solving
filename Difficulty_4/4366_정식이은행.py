import sys

sys.stdin = open('4366.txt')


# n진수-> 10진수로 바꾸기
def changeTo10(num: str, n: int):  # 숫자, 진수
    tmp = 0
    num = num[::-1]
    for i in range(len(num)):
        tmp += int(num[i]) * (n ** i)
    return tmp


T = int(input())
for tc in range(1, T + 1):
    two = input()
    three = input()
    two_candidates = set()
    three_candidates = set()

    # 이진수 한 자리 바뀌는 경우의 수 => 십진수로 바꿔서 set에 저장
    for i in range(len(two)):
        two_candidates.add(changeTo10(two[:i] + str((int(two[i]) + 1) % 2) + two[i+1:],2))

    # 삼진수 한 자리 바뀌는 경우의 수 => 십진수로 바꿔서 set에 저장
    for i in range(len(three)):
        for j in range(1, 3):
            three_candidates.add(changeTo10(three[:i] + str((int(three[i]) + j) % 3) + three[i+1:],3))

    # 같은 수가 정답!
    for t in two_candidates:
        if t in three_candidates:
            ans = t
            break
    print(f'#{tc} {ans}')