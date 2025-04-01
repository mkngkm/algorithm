# 동전 바꿔주기

# 첫째 줄에는 지폐의 금액 T(0<T≤10,000), 둘째 줄에는 동전의 가지 수 k(0<k≤10), 셋째 줄부터
# 마지막 줄까지는 각 줄에 동전의금액 pi(0<pi≤T)와 개수 ni(0<ni≤10)가 주어진다. pi와 ni 사이에는 빈 칸이 하나씩 있다.

# 첫 번째 줄에 동전 교환 방법의 가지 수를 출력한다.(교환할 수 없는 경우는 존재하지 않는다)

def dfs(L, sum):
    global cnt
    if sum > t:
        return
    if L == k:
        if sum == t:
            cnt += 1
    else:
        for i in range(n[L]+1): # 해당 동전 금액이 포함이 안된경우부터 다 쓴 경우까지 카운트
            dfs(L+1, sum + p[L] * i)

if __name__=="__main__":
    t = int(input())
    k = int(input())
    p = []
    n = []
    for _ in range(k):
        a, b = map(int, input().split())
        p.append(a)
        n.append(b)
    print(p)
    print(n)
    cnt = 0
    dfs(0, 0)
    print(cnt)
    