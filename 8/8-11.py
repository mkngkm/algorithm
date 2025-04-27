# 동전 교환

# ▣ 입력설명
# 첫 번째 줄에는 동전의 종류개수 N(1<=N<=12)이 주어진다. 두 번째 줄에는 N개의 동전의 종류가 주어지고, 그 다음줄에 거슬러 줄 금액 M(1<=M<=500)이 주어진다.
# 각 동전의 종류는 100원을 넘지 않는다.
# ▣ 출력설명
# 첫 번째 줄에 거슬러 줄 동전의 최소개수를 출력한다

if __name__=="__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    dy = [1000] * (m+1)
    dy[0] = 0
    for c in coin:
        for i in range(c, m+1):
            dy[i] = min(dy[i], dy[i-c] + 1)
    print(dy[m])
        
        
    