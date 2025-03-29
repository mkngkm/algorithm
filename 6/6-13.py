#경로 탐색(그래프 DFS)

# 첫째 줄에는 정점의 수 N(2<=N<=20)와 간선의 수 M가 주어진다. 
# 그 다음부터 M줄에 걸쳐 연결 정보가 주어진다. 

# 총 가지수를 출력한다.

def dfs(start):
    global cnt
    if start == n:
        cnt += 1
    else:
        for next in range(1, n+1):
            if a[start][next] == 1 and ch[next] == 0:
                ch[next] = 1
                dfs(next)
                ch[next] = 0      
    
        
n, m = map(int, input().split())

# 방향그래프 -> 인접 행렬
a = [ [0] * (n+1) for _ in range(n+1)]
ch = [0] * (n+1) # 이미 지나간 정점 체크 

for _ in range(m):
    i, j = map(int, input().split())
    a[i][j] = 1

# 1번 정점에서 n번 정점으로 가는 가지 수 
cnt = 0 
ch[1] = 1
dfs(1)
print(cnt)
