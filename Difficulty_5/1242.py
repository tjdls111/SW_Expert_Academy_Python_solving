# import sys
#
# sys.stdin = open('1242_input.txt')


hex_change = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',

}

secret_code = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9}


def change_to_hex(num):
    final = ''
    for ii in range(len(num)):
        final = final + hex_change[num[ii]]
    return final


def find_start():
    # 위 -> 아래, 오-> 왼 보면서 암호 코드의 시작 지점을 찾는다.
    start_candidates = []
    for i in range(1, N - 1):
        j = M * 4 - 1
        while j >= 56:
            if arr[i][j] == '1':
                # 암호코드(시작 지점)인지 보기
                if arr[i - 1][j] == '0' and arr[i][j + 1] == '0':  # 처음에 등장할 때만 볼 것
                    start_candidates.append((i, j))
                j -= 7
            else:
                j -= 1
    return start_candidates


def change_ratio(binary_num, ratio):
    final = ''
    if ratio == 1:
        return binary_num
    for k in range(0, 56 * ratio, ratio):
        # 그만큼 배로 했으면, 줄일 수 있어야 함.
        num = binary_num[k]
        for kk in range(k + 1, k + ratio):
            if num != binary_num[kk]:
                return False
        final = final + binary_num[k]
    return final

T = int(input().strip())
for tc in range(1, T + 1):

    N, M = map(int, input().strip().split())
    arr = list(change_to_hex(input().strip()) for _ in range(N))
    # 처음부터 16진수 -> 2진수

    secret_code_total = 0  # 정상적인 암호코드들에 포함된 숫자들의 합

    # 거꾸로 보다가 위 값이 0인지 확인 -> 시작점 후보로 넣기
    start_idx_candidates = find_start()

    for start_idx_candidate in start_idx_candidates:
        i = 0
        while start_idx_candidate[1] - 55 - 56 * i >= 0:  # 비율로 계산해야 함. 7 -> 14 -> 21 쭉 보기
            secret_code_candidate = ''.join(
                arr[start_idx_candidate[0]][start_idx_candidate[1] - 55 - 56 * i:start_idx_candidate[1] + 1])
            i += 1

            # 비율에 맞게 줄임
            tiny_binary_secret_code_candidate = change_ratio(secret_code_candidate, i)
            if tiny_binary_secret_code_candidate == False:
                continue

            else:
                # 암호 코드로 변환
                secret_code_s = []
                for k in range(0, 50, 7):
                    if secret_code.get(tiny_binary_secret_code_candidate[k:k + 7]) == None:
                        break
                    else:
                        secret_code_s.append(secret_code.get(tiny_binary_secret_code_candidate[k:k + 7]))
                # 검증 코드 확인하여 정상적인 암호 코드인지 확인
                if len(secret_code_s) == 8:
                    verification_code = (secret_code_s[0] + secret_code_s[2] + secret_code_s[4] + secret_code_s[
                        6]) * 3 + (secret_code_s[1] + secret_code_s[3] + secret_code_s[5]) + secret_code_s[7]

                    if verification_code % 10 == 0:
                        # 암호 코드 수 더하기
                        secret_code_total += sum(secret_code_s)

    print(f'#{tc} {secret_code_total}')
