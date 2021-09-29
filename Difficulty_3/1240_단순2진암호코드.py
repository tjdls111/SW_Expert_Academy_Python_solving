import sys, collections
sys.stdin = open('input.txt')

T = int(input())

secret_code = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}

def find_start():
    for i in range(N):
        for j in range(M-1, 55, -1):
            if arr[i][j] == '0':
                continue
            elif arr[i][j] == '1': # 7씩 잘라서 암호코드(시작 지점)인지 보기
                secret_code_candidate = ''.join(arr[i][j-6:j+1])
                # print(secret_code_candidate)
                if secret_code_candidate in secret_code.keys():

                    return (i,j, secret_code[secret_code_candidate])

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(list(input()) for _ in range(N))
    # 첫번째 암호 코드 찾기
    i, j, first_secret_code = find_start()
    ans = collections.deque()
    ans.append(first_secret_code)

    # 거기서부터 쭉 7번 더 보기
    for k in range(j-7, j-50, -7):
        secret_code_candidate = ''.join(arr[i][k-6:k+1])
        ans.appendleft(secret_code[secret_code_candidate])

    # 검증 코드
    verification_code = (ans[0]+ans[2]+ans[4]+ans[6])*3 + (ans[1]+ans[3]+ans[5]) + ans[7]
    if verification_code % 10 == 0: # 검증 코드가 제대로 되었으면
        print(f'#{tc} {sum(ans)}')
    else:
        print(f'#{tc} {0}')


