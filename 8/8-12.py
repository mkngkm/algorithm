# 최대점수 구하기(냅색 알고리즘)

# ▣ 입력설명
# 첫 번째 줄에 문제의 개수N(1<=N<=100)과 제한 시간 M(10<=M<=1000)이 주어집니다.
# 두 번째 줄부터 N줄에 걸쳐 문제를 풀었을 때의 점수와 푸는데 걸리는 시간이 주어집니다.
# ▣ 출력설명
# 첫 번째 줄에 제한 시간안에 얻을 수 있는 최대 점수를 출력합니다.



if __name__=="__main__":
    n, m = map(int, input().split())
    prob = list()
    dy = [0] * (m+1)
    for i in range(n):
        s, t = map(int, input().split())
        if t <= m:
            for j in range(m, t-1, -1): # 한문제를 여러번 풀 수 없다
                dy[j] = max(dy[j], dy[j-t] + s)
    print(dy[m])