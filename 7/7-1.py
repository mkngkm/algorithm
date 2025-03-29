# 최대 점수 구하기(DFS)

# 첫 번째 줄에 문제의 개수N(1<=N<=20)과 제한 시간 M(10<=M<=300)이 주어집니다.
# 두 번째 줄부터 N줄에 걸쳐 문제를 풀었을 때의 점수와 푸는데 걸리는 시간이 주어집니다.

# 첫 번째 줄에 제한 시간안에 얻을 수 있는 최대 점수를 출력합니다.
def dfs(L, tot, limit):
    global best
    # 시간 초과시 가지치기
    if limit > m:
        return
    if L == n:
        best = max(best,tot)
        return
    else:
        dfs(L+1, tot + score[L], limit + time[L])
        dfs(L+1, tot, limit)
            

if __name__=="__main__":
    n, m = map(int, input().split())
    score = [0] * n
    time = [0] * n
    
    for i in range(n):
        s, t = map(int, input().split()) # 점수, 시간
        score[i] = s
        time[i] = t
    best = 0
    dfs(0, 0, 0)
    print(best)
    