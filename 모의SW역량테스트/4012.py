import sys,copy
sys.stdin = open('4012_input.txt')

def nCr(n, r, s, k):
    if k == r:
        A.append(copy.copy(C))

        return
    else:
        for i in range(s, n - r + k + 1):
            C[k] = i
            nCr(n, r, i + 1, k + 1)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    foods = list(list(map(int,input().split())) for _ in range(N))

    C = [0] * (N//2)
    # A 음식에 넣을 재료를 A에 저장
    A = []
    nCr(N, N//2, 0, 0)

    # B 음식에 넣을 재료를 B에 저장
    B = []
    for i in range(len(A)//2): # A, B가 반대이고 똑같은 경우는 안 보려고 반만 봄
        C = []
        for j in range(N):
            if j not in A[i]:
                C.append(j)
        B.append(copy.copy(C))


    ans = 20000*16*16 # 두 음식 간 맛의 차이(최소가 정답)

    # 음식 맛 계산(2개씩 조합)
    for i in range(len(A)//2):
        A_deli = 0
        B_deli = 0
        # A에서 두 개 고르기
        for j in range(len(A[0])):
            for k in range(len(A[0])):
                # 음식 맛 계산
                A_deli += foods[A[i][j]][A[i][k]]
                B_deli += foods[B[i][j]][B[i][k]]

        ans = min(ans, abs(A_deli - B_deli))





    # nCr(A_comb, N//2, 2, 0,0)
    # nCr(B_comb, N//2, 2, 0,0)

    print(f'#{tc} {ans}')



