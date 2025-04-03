# 동전 분배하기

# 세 명에게 동전을 적절히 나누어 주어, 세 명이 받은 각각의 총액을 계산해, 총액이 가장 큰
# 사람과 가장 작은 사람의 차가 최소가 되도록 해보세요.
# 단 세 사람의 총액은 서로 달라야 합니다.

# 첫째 줄에는 동전의 개수 N(3<=N<=12)이 주어집니다.
# 그 다음 N줄에 걸쳐 각 동전의 금액이 주어집니다.

# 총액이 가장 큰 사람과 가장 작은 사람의 최소차를 출력하세요.(A, B, C)

def dfs(L, sumA, sumB, sumC):
    global res
    if L == n:
        if sumA > 0 and sumB > 0 and sumC > 0:
            if sumA != sumB and sumB != sumC and sumC != sumA:
                res = min(res, max(sumA, sumB, sumC) - min(sumA, sumB, sumC))                     
    else:
        dfs(L+1, sumA + coin[L], sumB, sumC)
        dfs(L+1, sumA, sumB + coin[L], sumC)
        dfs(L+1, sumA, sumB, sumC + coin[L])
        
if __name__=="__main__":
    n = int(input())
    coin = list()
    for _ in range(n):
        coin.append(int(input()))
    res = 21740000000
    answ = []
    dfs(0, 0, 0, 0)
    print(res)