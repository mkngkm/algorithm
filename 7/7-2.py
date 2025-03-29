# 휴가

#  상담은 상담을 완료하는데 걸리는 날수 T와 상담을 했을 때 받을 수 있는 금액 P로 이루어져 있다.

# 첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.
# 둘째 줄부터 1일부터 N일까지 순서대로 주어진다. (1 ≤ T ≤ 7, 1 ≤ P ≤ 100)

# 첫째 줄에 현수가 얻을 수 있는 최대 이익을 출력한다.

def dfs(L, amount): # last 는 마지막으로 더한 상담-> 빼버림(필요 없음)
    global best
    # 여행 날짜보다 상담이 완료되는 날짜가 길다면
    if L > n:
        return 
    if L == n:
        best = max(best, amount)
    else:
        # 혹은 여기서 날짜 넘어가는지 판별해도 됨. 
        dfs(L + t[L], amount + p[L]) # 현재 날짜 상담함
        dfs(L+1, amount) # 현재 날짜 상담 안함 -> 다음날에서 시작 # 얘 때문에 결국 n에 도달할 수 밖에 없대. 

if __name__=="__main__":
    n = int(input()) # N+1 일째에 휴가를 떠남, n 일 간의 일정이 주어짐
    t = [0] * n # 해당 상담을 완료하는데 걸리는 날수
    p = [0] * n # 해당 상담 후 받을 수 있는 금액
    for i in range(n):
        a, b = map(int, input().split())
        t[i] = a
        p[i] = b
    best = 0
    dfs(0, 0)
    print(best)      