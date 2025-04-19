# 알리바바와 40인의 도둑(Bottom-Up)

# ▣ 입력설명
# 첫 번째 줄에는 자연수 N(1<=N<=20)이 주어진다.
# 두 번째 줄부터 계곡의 N*N 격자의 돌다리 높이(10보다 작은 자연수) 정보가 주어진다.
# ▣ 출력설명
# 첫 번째 줄에 (1, 1)출발지에서 (N, N)도착지로 가기 위한 최소 에너지를 출력한다.

# 첫번째 가로줄 세로줄 다 채우고(가는 방법 1가지니까) 가운데는 위 왼쪽 비교해서 작은거 -> 수학문제 가는 길 찾는문제네..

if __name__=="__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0] * n for _ in range(n)]
    dy[0][0] = arr[0][0]
    for i in range(n):
        dy[0][i] = dy[0][i-1] + arr[0][i]
        dy[i][0] = dy[i-1][0] + arr[i][0]
    for i in range(1, n):
        for j in range(1, n):
            dy[i][j] = min(dy[i-1][j], dy[i][j-1]) + arr[i][j]
    print(dy[n-1][n-1])